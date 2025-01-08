from asyncio import timeout

import cudo_compute as cudo
import os
from time import sleep
import importlib.metadata
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import atexit
import threading

from cudo_compute.models.create_vm_response import CreateVMResponse
from cudo_compute.models.vm import VM

home = os.path.expanduser("~")

c = None


def make_client(key=None):
    configuration = cudo.Configuration()

    if key is None:
        key, err = get_api_key()
        if err:
            return None, err

    configuration.api_key['Authorization'] = key
    # configuration.debug = True
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    configuration.host = "https://rest.compute.cudo.org"

    client = cudo.ApiClient(configuration)
    version = ''
    try:
        version = importlib.metadata.version('cudo-compute')
    except:
        pass

    client.user_agent = 'cudo-compute-python-client/' + version
    return client, None


def get_api_key():
    key_config, context_config, error = cudo.AuthConfig.load_config(home + '/.config/cudo/cudo.yml', "")
    if not error:
        return key_config['key'], None
    else:
        return None, error


def get_project_id():
    key_config, context_config, error = cudo.AuthConfig.load_config(home + '/.config/cudo/cudo.yml', "")
    if not error:
        if 'project' in context_config:
            return context_config['project'], None
        else:
            return None, Exception('No project set in configuration (cudo.yml)')
    else:
        return None, error


def project_id():
    p, e = get_project_id()
    if e is None:
        return p
    return ''


def project_id_throwable():
    p, e = get_project_id()
    if e is None:
        return p
    else:
        raise e


def find_client(key=None):
    global c
    if c is None:
        c, err = make_client(key)
        if err:
            raise Exception(err)
    return c


def api_keys(key=None):
    return cudo.APIKeysApi(find_client(key))


def billing(key=None):
    return cudo.BillingApi(find_client(key))


def data_centers(key=None):
    return cudo.DataCentersApi(find_client(key))


def disks(key=None):
    return cudo.DisksApi(find_client(key))


def machine_types(key=None):
    return cudo.MachineTypesApi(find_client(key))


def networks(key=None):
    return cudo.NetworksApi(find_client(key))


def object_storage(key=None):
    return cudo.ObjectStorageApi(find_client(key))


def permissions(key=None):
    return cudo.PermissionsApi(find_client(key))


def projects(key=None):
    return cudo.ProjectsApi(find_client(key))


def ssh_keys(key=None):
    return cudo.SSHKeysApi(find_client(key))


def search(key=None):
    return cudo.SearchApi(find_client(key))


def user(key=None):
    return cudo.UserApi(find_client(key))


def legacy_virtual_machines(key=None):
        return cudo.VirtualMachinesApi(find_client(key))


class PooledVirtualMachinesApi(cudo.VirtualMachinesApi):
    def __init__(self, api_client=None):
        self.task_queue = None
        self.max_workers = 5
        self.shutdown_event = threading.Event()
        self.workers_active = False
        self.executor = None
        atexit.register(self.stop_workers)
        super().__init__(api_client)

    def create_vm(self, project_id, create_vm_body, **kwargs):
        self.start_queue()
        self.task_queue.put((project_id, create_vm_body))
        self.start_workers()
        return CreateVMResponse(id=create_vm_body.vm_id, vm=VM())

    def worker(self):
        while self.workers_active:
            if not self.task_queue:
                break
            req = self.task_queue.get(timeout=1)
            create_vm_body = None
            try:
                project, create_vm_body = req
                vm = super().create_vm(project, create_vm_body)
                print(f"Created VM: {vm.to_dict()}")
                wait = True
                while wait:
                    res = self.get_vm(project, create_vm_body.vm_id)
                    if (res.vm.state == 'ACTIVE' or res.vm.state == 'FAILED' or res.vm.state == 'STOPPED'
                            or res.vm.state == 'SUSPENDED' or res.vm.state == 'DELETED'):
                        wait = False
                    else:
                        sleep(5)
            except Exception as e:
                if create_vm_body:
                    print(f"Error creating VM: {create_vm_body.vm_id} {e}")
                else:
                    print(f"Error creating VM: {e}")

            self.task_queue.task_done()

    def start_queue(self):
        if not self.task_queue:
            self.task_queue = Queue()

    def start_workers(self):
        if not self.workers_active:
            self.workers_active = True
            self.executor = ThreadPoolExecutor(max_workers=self.max_workers)

            for _ in range(self.max_workers):
                self.executor.submit(self.worker)

    def stop_workers(self):
        if not self.shutdown_event.is_set():
            try:
                self.workers_active = False
                self.shutdown_event.set()

                if self.executor:
                    self.executor.shutdown(wait=False)

            except Exception as e:
                print(f"Error shutting down: {e}")


pool = None


def virtual_machines(key=None):
    global pool
    if pool is None:
        pool = PooledVirtualMachinesApi(find_client(key))
    return pool


def default(key = None):
    return cudo.DefaultApi(find_client(key))

import cudo_compute as cudo
import os
from time import sleep
import importlib.metadata
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import atexit
import threading

home = os.path.expanduser("~")


def client():
    configuration = cudo.Configuration()
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


# APIs
def api_keys():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.APIKeysApi(c)


def disks():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.DisksApi(c)


def networks():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.NetworksApi(c)


def object_storage():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.ObjectStorageApi(c)


def permissions():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.PermissionsApi(c)


def projects():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.ProjectsApi(c)


def ssh_keys():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.SSHKeysApi(c)


def search():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.SearchApi(c)


def user():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.UserApi(c)


class PooledVirtualMachinesApi(cudo.VirtualMachinesApi):
    def __init__(self, api_client=None):
        self.task_queue = None
        self.max_workers = 2
        self.shutdown_event = threading.Event()
        self.workers_active = False
        self.executor = None
        atexit.register(self.stop_workers)
        super().__init__(api_client)

    def create_vm(self, project_id, create_vm_body, **kwargs):
        self.start_queue()
        self.task_queue.put((project_id, create_vm_body))
        self.start_workers()
        return {"id": create_vm_body.vm_id}

    def worker(self):
        while self.workers_active:
            if not self.task_queue:
                break
            req = self.task_queue.get() # block true, timeout none
            create_vm_body = None
            try:
                project, create_vm_body = req
                vm = super().create_vm(project, create_vm_body)
                print(f"Created VM: {vm.to_dict()}")
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


c, err = client()
if err:
    raise Exception(err)
pool = PooledVirtualMachinesApi(c)


def virtual_machines():
    return pool

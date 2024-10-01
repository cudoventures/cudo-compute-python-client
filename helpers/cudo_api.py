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

class ExtendedVirtualMachinesApi(cudo.VirtualMachinesApi):
    def __init__(self, api_client=None):
        max_workers=2 #TODO make larger
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.task_queue = Queue()
        self.max_workers = max_workers
        self.shutdown_event = threading.Event()
        self.workers_active = False

        # Register the shutdown method to be called at exit
        atexit.register(self.shutdown)

        super().__init__(api_client)
        # Additional initialization if needed

    def start_workers(self):
        if not self.workers_active:
            self.workers_active = True
            self.shutdown_event.clear()
            for _ in range(self.max_workers):
                self.executor.submit(self.worker)
            print("Workers started.") #TODO

    def stop_workers(self):
        if self.workers_active:
            self.workers_active = False
            for _ in range(self.max_workers):
                self.task_queue.put(None)
            print("Workers stopped.") #TODO

    def worker(self):
        while True:
            req = self.task_queue.get()
            if req is None:
                break
            project, create_vm_body, kwargs = req
            super().create_vm(project, create_vm_body)
            self.task_queue.task_done()

            # Check if the task queue is empty and call shutdown if it is
            if self.task_queue.empty():
                self.shutdown()

    def create_vm(self, project_id, create_vm_body, **kwargs):
        print("Adding VM...") #TODO
        self.task_queue.put((project_id, create_vm_body))
        self.start_workers()

        # Custom implementation or additional logic
        print("Creating VM with custom logic")
        # return

    def shutdown(self):
        if not self.shutdown_event.is_set():
            self.shutdown_event.set()
            # Wait for all tasks to be processed
            self.task_queue.join()
            print("All VMs added. Waiting for all tasks to complete...")

            # Stop worker threads
            self.stop_workers()

            self.executor.shutdown(wait=True)
            print("Executor shutdown complete.")


def virtual_machines():
    c, err = client()
    if err:
        raise Exception(err)
    return ExtendedVirtualMachinesApi(c)

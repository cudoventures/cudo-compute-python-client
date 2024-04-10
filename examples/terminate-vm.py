from cudo_compute import cudo_api
from cudo_compute.rest import ApiException

try:
    api = cudo_api.virtual_machines()
    api.terminate_vm(cudo_api.project_id_throwable(), 'my-vm-id')
except ApiException as e:
    print(e)

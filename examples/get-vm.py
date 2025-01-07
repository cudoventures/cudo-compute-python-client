from cudo_compute import cudo_api
from cudo_compute.rest import ApiException
import json

api = cudo_api.virtual_machines()
project_id = cudo_api.project_id_throwable()

try:
    vm = api.get_vm(project_id, 'my-vm-id')
    print(vm.to_dict())
except ApiException as e:
    print(e)

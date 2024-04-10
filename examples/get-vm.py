from cudo_compute import cudo_api
from cudo_compute.rest import ApiException
import json

try:
    api = cudo_api.virtual_machines()
    vm = api.get_vm(cudo_api.project_id_throwable(), 'my-vm-id')
    print(vm.to_dict())
except ApiException as e:
    print(e)

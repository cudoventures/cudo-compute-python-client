from cudo_compute import cudo_api
from cudo_compute.rest import ApiException
import json

api = cudo_api.virtual_machines()

try:
    all_types = api.list_vm_machine_types2()
    print(json.dumps(all_types.to_dict(), indent=2))
except ApiException as e:
    print(e)

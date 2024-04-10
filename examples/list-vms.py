from cudo_compute import cudo_api
from cudo_compute.rest import ApiException
import json

try:
    api = cudo_api.virtual_machines()
    vms = api.list_vms(cudo_api.project_id_throwable())
    print(json.dumps(vms.to_dict(), indent=2))
except ApiException as e:
    print(e)

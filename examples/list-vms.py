from cudo_compute import cudo_api
from cudo_compute.rest import ApiException
import json

api = cudo_api.virtual_machines()
project_id = cudo_api.project_id_throwable()
try:
    vms = api.list_vms(project_id)
    print(json.dumps(vms.to_dict(), indent=2))
except ApiException as e:
    print(e)

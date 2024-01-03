from cudo_compute import cudo_api
from cudo_compute.rest import ApiException
import json

try:
    api = cudo_api.virtual_machines()
    images = api.list_public_vm_images()
    print(json.dumps(images.to_dict(), indent=2))
except ApiException as e:
    print(e)

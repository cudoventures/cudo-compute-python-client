from cudo_compute import cudo_api
from cudo_compute.rest import ApiException
import json

# In normal use the api key is automatically taken from cudoctl commandline tool,
# advanced users may want  to supply and api key without installing cudoctl.
# Below is an example of how to do that:

# Create your apis first
# When supplying your api key the vms api should only be created once per key.
api_key = "<KEY>"
vms_api = cudo_api.virtual_machines(api_key)
projects_api = cudo_api.projects(api_key)

# Remember to manually supply your project and not to get project id from the cudo_api
project_id = '<your-project-id>'
try:
    vms = vms_api.list_vms(project_id)
    print(json.dumps(vms.to_dict(), indent=2))
except ApiException as e:
    print(e)

try:
    projects = projects_api.list_projects()
except ApiException as e:
    print(e)

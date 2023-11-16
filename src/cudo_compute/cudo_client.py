import src.cudo_compute as cudo
def get_client():
    configuration = cudo.Configuration()
    key, err = cudo.AuthConfig.get_api_key()

    if err != None:
        return None, err

    configuration.api_key['Authorization'] = key
    # configuration.debug = True
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    configuration.host = "https://rest.compute.cudo.org"

    sclient = cudo.ApiClient(configuration)
    vms_api_client = cudo.VirtualMachinesApi(sclient)
    return vms_api_client, None
def get_client():
    configuration = client.Configuration()
    key, err = config.get_api_key()

    if err != None:
        return None, err

    configuration.api_key['Authorization'] = key
    # configuration.debug = True
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    configuration.host = "https://rest.compute.cudo.org"

    sclient = client.ApiClient(configuration)
    vms_api_client = client.VirtualMachinesApi(sclient)
    return vms_api_client, None
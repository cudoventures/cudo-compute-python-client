import cudo_compute as client
def get_client():
    configuration = client.Configuration()
    # key, err = config.get_api_key()

    # if err != None:
    #     return None, err

    configuration.api_key['Authorization'] = "derp"
    # configuration.debug = True
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    configuration.host = "https://rest.compute.cudo.org"

    sclient = client.ApiClient(configuration)
    vms_api_client = client.VirtualMachinesApi(sclient)
    return vms_api_client, None

def machine_types(gpu_model, mem_gib, vcpu_count, gpu_count):
    try:
        c, e = get_client()
        types = c.list_vm_machine_types(mem_gib, vcpu_count, gpu=gpu_count, gpu_model=gpu_model)
        types_dict = types.to_dict()
        return types_dict
    except Exception as e:  # TODO what to do with errors ?
        raise e


t = machine_types("",4,4,0)
print(t)
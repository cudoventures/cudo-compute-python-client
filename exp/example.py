import cudo_compute as cudo
def machine_types(gpu_model, mem_gib, vcpu_count, gpu_count):
    try:
        client, e = cudo.CudoClient.get_client()
        api = cudo.VirtualMachinesApi(client)
        types = api.list_vm_machine_types(mem_gib, vcpu_count, gpu=gpu_count, gpu_model=gpu_model)
        types_dict = types.to_dict()
        return types_dict
    except Exception as e:
        raise e


print(machine_types("",4,4,0))


def list_instances():
    try:
        project_id, e = cudo.AuthConfig.get_project()
        client, e = cudo.CudoClient.get_client()
        api = cudo.VirtualMachinesApi(client)
        vms = api.list_vms(project_id)
        instances = {}
        vms_dict = vms.to_dict()
        return vms_dict
    except Exception as e:
        raise e

print(list_instances())


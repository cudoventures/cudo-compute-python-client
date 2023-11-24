from cudo_compute import cudo_api
import cudo_compute


def machine_types(gpu_model, mem_gib, vcpu_count, gpu_count):
    try:
        api = cudo_api.virtualmachines()
        types = api.list_vm_machine_types(mem_gib, vcpu_count, gpu=gpu_count, gpu_model=gpu_model)
        types_dict = types.to_dict()
        return types_dict
    except Exception as e:
        raise e


print(machine_types("", 4, 4, 0))

print(cudo_api.project_id())

def list_instances():
    try:
        api = cudo_api.virtualmachines()
        vms = api.list_vms(cudo_api.project_id())
        instances = {}
        vms_dict = vms.to_dict()
        return vms_dict
    except Exception as e:
        raise e


print(list_instances())

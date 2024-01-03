from cudo_compute import cudo_api
from cudo_compute.rest import ApiException
import json


def machine_types(gpu_model, mem_gib, vcpu_count, gpu_count):
    try:
        api = cudo_api.virtual_machines()
        types = api.list_vm_machine_types(mem_gib, vcpu_count, gpu=gpu_count, gpu_model=gpu_model)
        types_dict = types.to_dict()
        return types_dict['host_configs']
    except ApiException as e:
        raise e


def gpu_types(gpu_count):
    try:
        api = cudo_api.virtual_machines()
        types = api.list_vm_machine_types(1, 1, gpu=gpu_count, )
        gpu_list = []
        for gpu in types.to_dict()['gpu_models']:
            gpu_list.append(gpu['name'])
        return gpu_list
    except ApiException as e:
        raise e


print('Gpu types')
print(json.dumps(gpu_types(1), indent=2))

print('Machine types with GPU')
mts = machine_types("", 1, 1, 1)
mt_list = []
for mt in mts:
    mt_list.append(
        {'machine_type': mt['machine_type'], 'gpu_model': mt['gpu_model'], 'data_center_id': mt['data_center_id']})
print(json.dumps(mt_list, indent=2))

print('Machine types without GPU')
mts = machine_types("", 1, 1, 0)
mt_list = []
for mt in mts:
    mt_list.append(
        {'machine_type': mt['machine_type'], 'data_center_id': mt['data_center_id']})
print(json.dumps(mt_list, indent=2))

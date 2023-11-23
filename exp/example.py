import cudo_compute as cudo
def machine_types(gpu_model, mem_gib, vcpu_count, gpu_count):
    try:
        c, e = cudo.CudoClient.get_client()
        types = c.list_vm_machine_types(mem_gib, vcpu_count, gpu=gpu_count, gpu_model=gpu_model)
        types_dict = types.to_dict()
        return types_dict
    except Exception as e:  # TODO what to do with errors ?
        raise e


t = machine_types("",4,4,0)
print(t)
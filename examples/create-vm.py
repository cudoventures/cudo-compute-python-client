from cudo_compute import cudo_api, Disk, CreateVMBody
from cudo_compute.rest import ApiException
import json

# Hint: use examples/machine-types.py to find machine_type/data_center_id and gpu_model
# use examples/images.py to get list of OS images for boot_disk_image_id
api = cudo_api.virtual_machines()
project_id = cudo_api.project_id_throwable()

try:
    disk = Disk(storage_class="STORAGE_CLASS_NETWORK", size_gib=100,
                id="my-disk-id")
    request = CreateVMBody(vm_id="my-vm-id", machine_type="epyc-rome-rtx-a4000",
                           data_center_id="no-luster-1", boot_disk_image_id='ubuntu-nvidia-docker',
                           memory_gib=16, vcpus=4, gpus=1, gpu_model="A4000", boot_disk=disk,
                           ssh_key_source='SSH_KEY_SOURCE_PROJECT',
                           metadata={"group": "a"})

    vm = api.create_vm(project_id, request)

    print(json.dumps(vm.to_dict(), indent=2))
except ApiException as e:
    print(e)

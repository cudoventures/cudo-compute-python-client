import sys
import os
from time import sleep

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'helpers')))

import cudo_api

from cudo_compute import Disk, CreateVMBody
from cudo_compute.rest import ApiException


vm_name = 'launch-lot'
id = 1
ids = []
api = cudo_api.virtual_machines()
try:
    for i in range(12):
        vm_id = vm_name + str(id)
        disk = Disk(storage_class="STORAGE_CLASS_NETWORK", size_gib=100,
                    id="my-disk-id-" + vm_id)

        request = CreateVMBody(vm_id=vm_id, machine_type="intel-broadwell",
                               data_center_id="gb-bournemouth-1", boot_disk_image_id='ubuntu-nvidia-docker',
                               memory_gib=4, vcpus=2, gpus=0, gpu_model="", boot_disk=disk)

        vm = api.create_vm(cudo_api.project_id_throwable(), request)
        print(vm)
        ids.append(vm_id)
        id += 1

except ApiException as e:
    print(e)

sleep(80)
for del_id in ids:
    res = api.terminate_vm(cudo_api.project_id_throwable(), del_id)
    print(res)

print("done")

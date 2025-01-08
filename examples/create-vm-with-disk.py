from cudo_compute import cudo_api, Disk, CreateVMBody, CreateStorageDiskBody
from cudo_compute.rest import ApiException
import json, time


# Define the VM and disk IDs and project ID.
vm_id = "my-vm"
disk_id = "my-storage_disk"
project_id = "my-project"
api_key = "da6daa76d5a765d7a"
data_center_id="gb-bournemouth-1"

# Create the APIs
vm_api = cudo_api.virtual_machines(api_key)
disk_api = cudo_api.disks(api_key)

def create_and_attach_disk():
    # Create a storage disk.
    disk = Disk(storage_class="STORAGE_CLASS_NETWORK", size_gib=100, id=disk_id)
    disk_request = CreateStorageDiskBody(data_center_id=data_center_id, disk=disk)
    disk = disk_api.create_storage_disk(project_id, disk_request)

    print(f"Disk created: {disk}")
    # Wait for the disk to be READY.
    disk = disk_api.get_disk(project_id, disk_id)
    while disk.disk.disk_state!= "DISK_STATE_READY":
        try:
            disk = disk_api.get_disk(project_id, disk_id)
            print(f"Waiting for disk to be READY... Current state: {disk.disk.state}")
        except Exception as e:
            print(f"Error getting disk: {e}")
            print(f"Retrying in 5 seconds...")
        time.sleep(5)

    # Attach the disk to the VM.
    res = disk_api.attach_storage_disk(project_id, disk_id,vm_id=vm_id)
    print(f"Disk attached: {res}")


try:
    # boot disk
    disk = Disk(storage_class="STORAGE_CLASS_NETWORK", size_gib=100,
                id="my-disk-id")
    request = CreateVMBody(vm_id=vm_id, machine_type="intel-broadwell",
                           data_center_id=data_center_id, boot_disk_image_id='ubuntu-2204-desktop',
                           memory_gib=16, vcpus=4, boot_disk=disk, gpus=0, ssh_key_source='SSH_KEY_SOURCE_PROJECT') # gpu_model=""
    # create vm
    vm = vm_api.create_vm(project_id, request)

    ## VM must be stopped or running before attaching disk, so wait for active state
    # https://github.com/cudoventures/cudo-compute-python-client/blob/main/docs/src/cudo_compute/models/vm_state.py
    while vm.vm.state!= "ACTIVE":
        try:
            vm = vm_api.get_vm(project_id, vm_id)
            print(f"Waiting for VM to be RUNNING... Current state: {vm.vm.state}")
        except Exception as e:
            print(f"Error getting VM: {e}")
            print(f"Retrying in 5 seconds...")
        time.sleep(5)

    # vm is running, create and attach disk
    create_and_attach_disk()
except ApiException as e:
    print(e)
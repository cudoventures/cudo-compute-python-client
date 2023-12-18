# CreateVMBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_disk** | [**Disk**](Disk.md) |  | [optional] 
**boot_disk_image_id** | **str** |  | 
**cpu_model** | **str** |  | [optional] 
**custom_ssh_keys** | **list[str]** |  | [optional] 
**data_center_id** | **str** |  | [optional] 
**gpu_model** | **str** |  | [optional] 
**gpus** | **int** |  | [optional] 
**machine_type** | **str** |  | [optional] 
**max_price_hr** | [**Decimal**](Decimal.md) |  | [optional] 
**memory_gib** | **int** |  | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**nics** | [**list[CreateVMRequestNIC]**](CreateVMRequestNIC.md) |  | [optional] 
**password** | **str** |  | [optional] 
**security_group_ids** | **list[str]** |  | [optional] 
**ssh_key_source** | [**SshKeySource**](SshKeySource.md) |  | [optional] 
**start_script** | **str** |  | [optional] 
**storage_disk_ids** | **list[str]** |  | [optional] 
**vcpus** | **int** |  | [optional] 
**vm_id** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



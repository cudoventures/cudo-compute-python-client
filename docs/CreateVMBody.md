# CreateVMBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_center_id** | **str** |  | 
**machine_type** | **str** |  | 
**vm_id** | **str** |  | 
**start_script** | **str** |  | [optional] 
**ssh_key_source** | [**SshKeySource**](SshKeySource.md) |  | [optional] 
**custom_ssh_keys** | **list[str]** |  | [optional] 
**password** | **str** |  | [optional] 
**boot_disk** | [**Disk**](Disk.md) |  | [optional] 
**boot_disk_image_id** | **str** |  | 
**vcpus** | **int** |  | 
**memory_gib** | **int** |  | 
**gpus** | **int** |  | 
**cpu_model** | **str** |  | [optional] 
**gpu_model** | **str** |  | [optional] 
**gpu_model_id** | **str** |  | [optional] 
**nics** | [**list[CreateVMRequestNIC]**](CreateVMRequestNIC.md) |  | [optional] 
**security_group_ids** | **list[str]** |  | [optional] 
**storage_disk_ids** | **list[str]** |  | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**topology** | [**CpuTopology**](CpuTopology.md) |  | [optional] 
**validate_only** | **bool** |  | [optional] 
**expire_time** | **datetime** |  | [optional] 
**ttl** | **str** |  | [optional] 
**commitment_term** | [**CommitmentTerm**](CommitmentTerm.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



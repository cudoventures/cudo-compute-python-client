# VM

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter_id** | **str** |  | [optional] 
**machine_type** | **str** |  | [optional] 
**region_id** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**external_ip_address** | **str** |  | [optional] 
**internal_ip_address** | **str** |  | [optional] 
**public_ip_address** | **str** |  | [optional] 
**memory** | **int** |  | [optional] 
**cpu_model** | **str** |  | [optional] 
**vcpus** | **int** |  | [optional] 
**gpu_model** | **str** |  | [optional] 
**gpu_model_id** | **str** |  | [optional] 
**gpu_quantity** | **int** |  | [optional] 
**boot_disk_size_gib** | **int** |  | [optional] 
**renewable_energy** | **bool** |  | [optional] 
**image_id** | **str** |  | [optional] 
**public_image_id** | **str** |  | [optional] 
**public_image_name** | **str** |  | [optional] 
**private_image_id** | **str** |  | [optional] 
**image_name** | **str** |  | [optional] 
**create_by** | **str** |  | [optional] 
**nics** | [**list[VMNIC]**](VMNIC.md) |  | [optional] 
**rules** | [**list[SecurityGroupRule]**](SecurityGroupRule.md) |  | [optional] 
**security_group_ids** | **list[str]** |  | [optional] 
**short_state** | **str** |  | [optional] 
**boot_disk** | [**Disk**](Disk.md) |  | [optional] 
**storage_disks** | [**list[Disk]**](Disk.md) |  | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**state** | [**VmState**](VmState.md) |  | [optional] 
**create_time** | **datetime** |  | [optional] 
**expire_time** | **datetime** |  | [optional] 
**price** | [**VMPrice**](VMPrice.md) |  | 
**commitment_term** | [**CommitmentTerm**](CommitmentTerm.md) |  | 
**commitment_end_time** | **datetime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



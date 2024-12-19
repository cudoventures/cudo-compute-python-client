# ListVMMachineTypesResponseVMMachineType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_center_id** | **str** |  | 
**machine_type** | **str** |  | 
**cpu_model** | **str** |  | 
**gpu_model** | **str** |  | 
**gpu_model_id** | **str** |  | 
**min_vcpu_per_memory_gib** | **float** |  | 
**max_vcpu_per_memory_gib** | **float** |  | 
**min_vcpu_per_gpu** | **float** |  | 
**max_vcpu_per_gpu** | **float** |  | 
**vcpu_price_hr** | [**Decimal**](Decimal.md) |  | 
**memory_gib_price_hr** | [**Decimal**](Decimal.md) |  | 
**gpu_price_hr** | [**Decimal**](Decimal.md) |  | 
**min_storage_gib_price_hr** | [**Decimal**](Decimal.md) |  | 
**ipv4_price_hr** | [**Decimal**](Decimal.md) |  | 
**renewable_energy** | **bool** |  | 
**max_vcpu_free** | **int** |  | 
**total_vcpu_free** | **int** |  | 
**max_memory_gib_free** | **int** |  | 
**total_memory_gib_free** | **int** |  | 
**max_gpu_free** | **int** |  | 
**total_gpu_free** | **int** |  | 
**max_storage_gib_free** | **int** |  | 
**total_storage_gib_free** | **int** |  | 
**min_vcpu** | **float** |  | 
**min_memory_gib** | **float** |  | 
**prices** | [**list[VMMachineTypeMachineTypePrice]**](VMMachineTypeMachineTypePrice.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



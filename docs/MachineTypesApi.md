# src.cudo_compute.MachineTypesApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_machine_type**](MachineTypesApi.md#get_machine_type) | **GET** /v1/data-centers/{dataCenterId}/machine-types/{machineType} | Get a machine type in a data center
[**get_machine_type_live_utilization**](MachineTypesApi.md#get_machine_type_live_utilization) | **GET** /v1/data-centers/{dataCenterId}/machine-types/{machineType}/live-utilization | Get the utilization for a machine type in a data center
[**list_machine_types**](MachineTypesApi.md#list_machine_types) | **GET** /v1/data-centers/{dataCenterId}/machine-types | List machine types for a data center


# **get_machine_type**
> GetMachineTypeResponse get_machine_type(data_center_id, machine_type)

Get a machine type in a data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.MachineTypesApi()
data_center_id = 'data_center_id_example' # str | 
machine_type = 'machine_type_example' # str | 

try:
    # Get a machine type in a data center
    api_response = api_instance.get_machine_type(data_center_id, machine_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineTypesApi->get_machine_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 
 **machine_type** | **str**|  | 

### Return type

[**GetMachineTypeResponse**](GetMachineTypeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_machine_type_live_utilization**
> GetMachineTypeLiveUtilizationResponse get_machine_type_live_utilization(data_center_id, machine_type)

Get the utilization for a machine type in a data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.MachineTypesApi()
data_center_id = 'data_center_id_example' # str | 
machine_type = 'machine_type_example' # str | 

try:
    # Get the utilization for a machine type in a data center
    api_response = api_instance.get_machine_type_live_utilization(data_center_id, machine_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineTypesApi->get_machine_type_live_utilization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 
 **machine_type** | **str**|  | 

### Return type

[**GetMachineTypeLiveUtilizationResponse**](GetMachineTypeLiveUtilizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_machine_types**
> ListMachineTypesResponse list_machine_types(data_center_id)

List machine types for a data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.MachineTypesApi()
data_center_id = 'data_center_id_example' # str | 

try:
    # List machine types for a data center
    api_response = api_instance.list_machine_types(data_center_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineTypesApi->list_machine_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 

### Return type

[**ListMachineTypesResponse**](ListMachineTypesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


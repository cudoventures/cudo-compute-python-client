# src.cudo_compute.DefaultApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_center_commitment_schedule**](DefaultApi.md#get_data_center_commitment_schedule) | **GET** /v1/data-centers/{dataCenterId}/commitment-schedule | 
[**get_data_center_commitment_time_series**](DefaultApi.md#get_data_center_commitment_time_series) | **GET** /v1/data-centers/{dataCenterId}/commitment-time-series | 
[**list_billing_account_projects**](DefaultApi.md#list_billing_account_projects) | **GET** /v1/billing-accounts/{id}/projects | 
[**list_data_center_machine_type_prices**](DefaultApi.md#list_data_center_machine_type_prices) | **GET** /v1/data-centers/{dataCenterId}/machine-type-prices | 
[**list_vm_machine_types**](DefaultApi.md#list_vm_machine_types) | **GET** /v1/vms/machine-types | 
[**search_resources**](DefaultApi.md#search_resources) | **GET** /v1/resources/search | 
[**track**](DefaultApi.md#track) | **POST** /v1/auth/track | 
[**update_vm_expire_time**](DefaultApi.md#update_vm_expire_time) | **POST** /v1/projects/{projectId}/vm/{id}/expire-time | 
[**update_vm_password**](DefaultApi.md#update_vm_password) | **POST** /v1/projects/{projectId}/vm/{id}/password | 


# **get_data_center_commitment_schedule**
> GetDataCenterCommitmentScheduleResponse get_data_center_commitment_schedule(data_center_id, start_time, end_time)



### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DefaultApi()
data_center_id = 'data_center_id_example' # str | 
start_time = '2013-10-20T19:20:30+01:00' # datetime | 
end_time = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.get_data_center_commitment_schedule(data_center_id, start_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_data_center_commitment_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 
 **start_time** | **datetime**|  | 
 **end_time** | **datetime**|  | 

### Return type

[**GetDataCenterCommitmentScheduleResponse**](GetDataCenterCommitmentScheduleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_center_commitment_time_series**
> GetDataCenterCommitmentTimeSeriesResponse get_data_center_commitment_time_series(data_center_id, start_time, end_time, interval)



### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DefaultApi()
data_center_id = 'data_center_id_example' # str | 
start_time = '2013-10-20T19:20:30+01:00' # datetime | 
end_time = '2013-10-20T19:20:30+01:00' # datetime | 
interval = 'INTERVAL_UNKNOWN' # str |  (default to INTERVAL_UNKNOWN)

try:
    api_response = api_instance.get_data_center_commitment_time_series(data_center_id, start_time, end_time, interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_data_center_commitment_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 
 **start_time** | **datetime**|  | 
 **end_time** | **datetime**|  | 
 **interval** | **str**|  | [default to INTERVAL_UNKNOWN]

### Return type

[**GetDataCenterCommitmentTimeSeriesResponse**](GetDataCenterCommitmentTimeSeriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_billing_account_projects**
> ListBillingAccountProjectsResponse list_billing_account_projects(id)



### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DefaultApi()
id = 'id_example' # str | string page_token = 2;  int32 page_size = 3;

try:
    api_response = api_instance.list_billing_account_projects(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_billing_account_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| string page_token &#x3D; 2;  int32 page_size &#x3D; 3; | 

### Return type

[**ListBillingAccountProjectsResponse**](ListBillingAccountProjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_center_machine_type_prices**
> ListDataCenterMachineTypePricesResponse list_data_center_machine_type_prices(data_center_id)



### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DefaultApi()
data_center_id = 'data_center_id_example' # str | 

try:
    api_response = api_instance.list_data_center_machine_type_prices(data_center_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_data_center_machine_type_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 

### Return type

[**ListDataCenterMachineTypePricesResponse**](ListDataCenterMachineTypePricesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vm_machine_types**
> ListVMMachineTypesResponse list_vm_machine_types()



### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DefaultApi()

try:
    api_response = api_instance.list_vm_machine_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_vm_machine_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVMMachineTypesResponse**](ListVMMachineTypesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_resources**
> SearchResourcesResponse search_resources(query)



### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DefaultApi()
query = 'query_example' # str | 

try:
    api_response = api_instance.search_resources(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 

### Return type

[**SearchResourcesResponse**](SearchResourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track**
> object track(track_body)



### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DefaultApi()
track_body = src.cudo_compute.TrackRequest() # TrackRequest | 

try:
    api_response = api_instance.track(track_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_body** | [**TrackRequest**](TrackRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vm_expire_time**
> UpdateVMExpireTimeResponse update_vm_expire_time(project_id, id, update_vm_expire_time_body)



### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DefaultApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
update_vm_expire_time_body = src.cudo_compute.UpdateVMExpireTimeBody() # UpdateVMExpireTimeBody | 

try:
    api_response = api_instance.update_vm_expire_time(project_id, id, update_vm_expire_time_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_vm_expire_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **update_vm_expire_time_body** | [**UpdateVMExpireTimeBody**](UpdateVMExpireTimeBody.md)|  | 

### Return type

[**UpdateVMExpireTimeResponse**](UpdateVMExpireTimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vm_password**
> UpdateVMPasswordResponse update_vm_password(project_id, id, update_vm_password_body)



### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DefaultApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
update_vm_password_body = src.cudo_compute.UpdateVMPasswordBody() # UpdateVMPasswordBody | 

try:
    api_response = api_instance.update_vm_password(project_id, id, update_vm_password_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_vm_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **update_vm_password_body** | [**UpdateVMPasswordBody**](UpdateVMPasswordBody.md)|  | 

### Return type

[**UpdateVMPasswordResponse**](UpdateVMPasswordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


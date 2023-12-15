# src.cudo_compute.PermissionsApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_billing_account_user_permission**](PermissionsApi.md#add_billing_account_user_permission) | **POST** /v1/billing-accounts/{billingAccountId}/add-user-permission | Add billing account user
[**add_data_center_user_permission**](PermissionsApi.md#add_data_center_user_permission) | **POST** /v1/data-centers/{dataCenterId}/add-user-permission | Add data center user
[**add_project_user_permission**](PermissionsApi.md#add_project_user_permission) | **POST** /v1/projects/{projectId}/add-user-permission | Add project user
[**list_user_permissions**](PermissionsApi.md#list_user_permissions) | **GET** /v1/auth/permissions | List
[**remove_billing_account_user_permission**](PermissionsApi.md#remove_billing_account_user_permission) | **POST** /v1/billing-accounts/{billingAccountId}/remove-user-permission | Remove billing account user
[**remove_data_center_user_permission**](PermissionsApi.md#remove_data_center_user_permission) | **POST** /v1/data-centers/{dataCenterId}/remove-user-permission | Remove data center user
[**remove_project_user_permission**](PermissionsApi.md#remove_project_user_permission) | **POST** /v1/projects/{projectId}/remove-user-permission | Remove project user


# **add_billing_account_user_permission**
> object add_billing_account_user_permission(billing_account_id, body)

Add billing account user

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.PermissionsApi()
billing_account_id = 'billing_account_id_example' # str | 
body = src.cudo_compute.Body1() # Body1 | 

try:
    # Add billing account user
    api_response = api_instance.add_billing_account_user_permission(billing_account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->add_billing_account_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_account_id** | **str**|  | 
 **body** | [**Body1**](Body1.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_data_center_user_permission**
> object add_data_center_user_permission(data_center_id, body)

Add data center user

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.PermissionsApi()
data_center_id = 'data_center_id_example' # str | 
body = src.cudo_compute.Body3() # Body3 | 

try:
    # Add data center user
    api_response = api_instance.add_data_center_user_permission(data_center_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->add_data_center_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 
 **body** | [**Body3**](Body3.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project_user_permission**
> object add_project_user_permission(project_id, body)

Add project user

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.PermissionsApi()
project_id = 'project_id_example' # str | 
body = src.cudo_compute.Body5() # Body5 | 

try:
    # Add project user
    api_response = api_instance.add_project_user_permission(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->add_project_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **body** | [**Body5**](Body5.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_permissions**
> ListUserPermissionsResponse list_user_permissions(project_id=project_id, data_center_id=data_center_id, billing_account_id=billing_account_id)

List

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.PermissionsApi()
project_id = 'project_id_example' # str |  (optional)
data_center_id = 'data_center_id_example' # str |  (optional)
billing_account_id = 'billing_account_id_example' # str |  (optional)

try:
    # List
    api_response = api_instance.list_user_permissions(project_id=project_id, data_center_id=data_center_id, billing_account_id=billing_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->list_user_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | [optional] 
 **data_center_id** | **str**|  | [optional] 
 **billing_account_id** | **str**|  | [optional] 

### Return type

[**ListUserPermissionsResponse**](ListUserPermissionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_billing_account_user_permission**
> object remove_billing_account_user_permission(billing_account_id, body)

Remove billing account user

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.PermissionsApi()
billing_account_id = 'billing_account_id_example' # str | 
body = src.cudo_compute.Body2() # Body2 | 

try:
    # Remove billing account user
    api_response = api_instance.remove_billing_account_user_permission(billing_account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->remove_billing_account_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_account_id** | **str**|  | 
 **body** | [**Body2**](Body2.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_data_center_user_permission**
> object remove_data_center_user_permission(data_center_id, body)

Remove data center user

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.PermissionsApi()
data_center_id = 'data_center_id_example' # str | 
body = src.cudo_compute.Body4() # Body4 | 

try:
    # Remove data center user
    api_response = api_instance.remove_data_center_user_permission(data_center_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->remove_data_center_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 
 **body** | [**Body4**](Body4.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project_user_permission**
> object remove_project_user_permission(project_id, body)

Remove project user

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.PermissionsApi()
project_id = 'project_id_example' # str | 
body = src.cudo_compute.Body11() # Body11 | 

try:
    # Remove project user
    api_response = api_instance.remove_project_user_permission(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->remove_project_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **body** | [**Body11**](Body11.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


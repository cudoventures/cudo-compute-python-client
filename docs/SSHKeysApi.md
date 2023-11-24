# src.cudo_compute.SSHKeysApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ssh_key**](SSHKeysApi.md#create_ssh_key) | **POST** /v1/ssh-keys | Create
[**delete_ssh_key**](SSHKeysApi.md#delete_ssh_key) | **DELETE** /v1/ssh-keys/{id} | Delete
[**get_ssh_key**](SSHKeysApi.md#get_ssh_key) | **GET** /v1/ssh-keys/{id} | Get
[**list_ssh_keys**](SSHKeysApi.md#list_ssh_keys) | **GET** /v1/ssh-keys | List


# **create_ssh_key**
> SshKey create_ssh_key(ssh_key)

Create

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.SSHKeysApi()
ssh_key = src.cudo_compute.SshKey() # SshKey | 

try:
    # Create
    api_response = api_instance.create_ssh_key(ssh_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSHKeysApi->create_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key** | [**SshKey**](SshKey.md)|  | 

### Return type

[**SshKey**](SshKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ssh_key**
> object delete_ssh_key(id)

Delete

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.SSHKeysApi()
id = 'id_example' # str | 

try:
    # Delete
    api_response = api_instance.delete_ssh_key(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSHKeysApi->delete_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssh_key**
> SshKey get_ssh_key(id)

Get

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.SSHKeysApi()
id = 'id_example' # str | 

try:
    # Get
    api_response = api_instance.get_ssh_key(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSHKeysApi->get_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SshKey**](SshKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ssh_keys**
> ListSshKeysResponse list_ssh_keys(page_number=page_number, page_size=page_size)

List

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.SSHKeysApi()
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # List
    api_response = api_instance.list_ssh_keys(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSHKeysApi->list_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**ListSshKeysResponse**](ListSshKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


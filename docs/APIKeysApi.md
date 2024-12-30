# src.cudo_compute.APIKeysApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_key**](APIKeysApi.md#delete_api_key) | **DELETE** /v1/api-keys/{name} | Delete
[**generate_api_key**](APIKeysApi.md#generate_api_key) | **POST** /v1/api-keys | Generate
[**list_api_keys**](APIKeysApi.md#list_api_keys) | **GET** /v1/api-keys | List


# **delete_api_key**
> object delete_api_key(name)

Delete

Deletes an API key, revoking all access for requests that use the key.

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.APIKeysApi()
name = 'name_example' # str | 

try:
    # Delete
    api_response = api_instance.delete_api_key(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_api_key**
> ApiKey generate_api_key(generate_api_key_body)

Generate

Creates a new API key for the requesting user. The API key is returned in the response, and this is the only time it can be viewed.

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.APIKeysApi()
generate_api_key_body = src.cudo_compute.GenerateApiKeyRequest() # GenerateApiKeyRequest | 

try:
    # Generate
    api_response = api_instance.generate_api_key(generate_api_key_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->generate_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_api_key_body** | [**GenerateApiKeyRequest**](GenerateApiKeyRequest.md)|  | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> ListApiKeysResponse list_api_keys(page_number=page_number, page_size=page_size)

List

List the details of all API keys created by the requesting user. This does not include the API key itself which is only visible once when the API key is created.

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.APIKeysApi()
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # List
    api_response = api_instance.list_api_keys(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->list_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**ListApiKeysResponse**](ListApiKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


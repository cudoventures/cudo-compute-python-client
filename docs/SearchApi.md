# src.cudo_compute.SearchApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_regions**](SearchApi.md#list_regions) | **GET** /v1/regions | Regions


# **list_regions**
> ListRegionsResponse list_regions()

Regions

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.SearchApi()

try:
    # Regions
    api_response = api_instance.list_regions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->list_regions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListRegionsResponse**](ListRegionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


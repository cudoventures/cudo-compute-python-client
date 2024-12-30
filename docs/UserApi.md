# src.cudo_compute.UserApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_verification_session**](UserApi.md#create_identity_verification_session) | **GET** /v1/auth/create-identity-verification-session | Get identity verification session
[**delete_user**](UserApi.md#delete_user) | **DELETE** /v1/auth | Delete
[**get**](UserApi.md#get) | **GET** /v1/auth | Get


# **create_identity_verification_session**
> IdentityVerificationSession create_identity_verification_session()

Get identity verification session

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.UserApi()

try:
    # Get identity verification session
    api_response = api_instance.create_identity_verification_session()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_identity_verification_session: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentityVerificationSession**](IdentityVerificationSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> object delete_user()

Delete

Deletes your user, deleting all records of your user, and revoking access to every resource.

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.UserApi()

try:
    # Delete
    api_response = api_instance.delete_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Profile get()

Get

Responds with details of the user when suitable authentication material is sent with the request.

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.UserApi()

try:
    # Get
    api_response = api_instance.get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


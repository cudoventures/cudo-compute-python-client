# src.cudo_compute.NetworksApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network**](NetworksApi.md#create_network) | **POST** /v1/projects/{projectId}/networks | Create network
[**create_security_group**](NetworksApi.md#create_security_group) | **POST** /v1/projects/{securityGroup.projectId}/networks/security-groups | Create security group
[**delete_network**](NetworksApi.md#delete_network) | **DELETE** /v1/projects/{projectId}/networks/{id} | Delete network
[**delete_security_group**](NetworksApi.md#delete_security_group) | **DELETE** /v1/projects/{projectId}/networks/security-groups/{id} | Delete security group
[**get_network**](NetworksApi.md#get_network) | **GET** /v1/projects/{projectId}/networks/{id} | Get network
[**get_security_group**](NetworksApi.md#get_security_group) | **GET** /v1/projects/{projectId}/networks/security-groups/{id} | Get a security group
[**list_networks**](NetworksApi.md#list_networks) | **GET** /v1/projects/{projectId}/networks | List networks
[**list_security_groups**](NetworksApi.md#list_security_groups) | **GET** /v1/projects/{projectId}/networks/security-groups | List security groups
[**start_network**](NetworksApi.md#start_network) | **POST** /v1/projects/{projectId}/networks/{id}/start | Start network
[**stop_network**](NetworksApi.md#stop_network) | **POST** /v1/projects/{projectId}/networks/{id}/stop | Stop network
[**update_security_group**](NetworksApi.md#update_security_group) | **PATCH** /v1/projects/{securityGroup.projectId}/networks/security-groups/{securityGroup.id} | Update security group


# **create_network**
> CreateNetworkResponse create_network(project_id, create_network_body)

Create network

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
project_id = 'project_id_example' # str | 
create_network_body = src.cudo_compute.CreateNetworkBody() # CreateNetworkBody | 

try:
    # Create network
    api_response = api_instance.create_network(project_id, create_network_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->create_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_network_body** | [**CreateNetworkBody**](CreateNetworkBody.md)|  | 

### Return type

[**CreateNetworkResponse**](CreateNetworkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_security_group**
> CreateSecurityGroupResponse create_security_group(security_group_project_id, security_group)

Create security group

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
security_group_project_id = 'security_group_project_id_example' # str | 
security_group = src.cudo_compute.SecurityGroup() # SecurityGroup | 

try:
    # Create security group
    api_response = api_instance.create_security_group(security_group_project_id, security_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->create_security_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_group_project_id** | **str**|  | 
 **security_group** | [**SecurityGroup**](SecurityGroup.md)|  | 

### Return type

[**CreateSecurityGroupResponse**](CreateSecurityGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network**
> DeleteNetworkResponse delete_network(project_id, id)

Delete network

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Delete network
    api_response = api_instance.delete_network(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->delete_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**DeleteNetworkResponse**](DeleteNetworkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_security_group**
> DeleteSecurityGroupResponse delete_security_group(project_id, id)

Delete security group

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Delete security group
    api_response = api_instance.delete_security_group(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->delete_security_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**DeleteSecurityGroupResponse**](DeleteSecurityGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network**
> GetNetworkResponse get_network(project_id, id)

Get network

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Get network
    api_response = api_instance.get_network(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->get_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GetNetworkResponse**](GetNetworkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_group**
> GetSecurityGroupResponse get_security_group(project_id, id)

Get a security group

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Get a security group
    api_response = api_instance.get_security_group(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->get_security_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GetSecurityGroupResponse**](GetSecurityGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_networks**
> ListNetworksResponse list_networks(project_id, page_number=page_number, page_size=page_size)

List networks

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
project_id = 'project_id_example' # str | 
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # List networks
    api_response = api_instance.list_networks(project_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->list_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**ListNetworksResponse**](ListNetworksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_security_groups**
> ListSecurityGroupsResponse list_security_groups(project_id, data_center_id=data_center_id, page_number=page_number, page_size=page_size)

List security groups

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
project_id = 'project_id_example' # str | 
data_center_id = 'data_center_id_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # List security groups
    api_response = api_instance.list_security_groups(project_id, data_center_id=data_center_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->list_security_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_center_id** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**ListSecurityGroupsResponse**](ListSecurityGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_network**
> StartNetworkResponse start_network(project_id, id)

Start network

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Start network
    api_response = api_instance.start_network(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->start_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**StartNetworkResponse**](StartNetworkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_network**
> StopNetworkResponse stop_network(project_id, id)

Stop network

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Stop network
    api_response = api_instance.stop_network(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->stop_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**StopNetworkResponse**](StopNetworkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_security_group**
> UpdateSecurityGroupResponse update_security_group(security_group_project_id, security_group_id, security_group)

Update security group

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.NetworksApi()
security_group_project_id = 'security_group_project_id_example' # str | 
security_group_id = 'security_group_id_example' # str | 
security_group = src.cudo_compute.SecurityGroup1() # SecurityGroup1 | 

try:
    # Update security group
    api_response = api_instance.update_security_group(security_group_project_id, security_group_id, security_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->update_security_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_group_project_id** | **str**|  | 
 **security_group_id** | **str**|  | 
 **security_group** | [**SecurityGroup1**](SecurityGroup1.md)|  | 

### Return type

[**UpdateSecurityGroupResponse**](UpdateSecurityGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


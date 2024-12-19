# src.cudo_compute.ProjectsApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /v1/projects | Create
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /v1/projects/{id} | Delete
[**get_project**](ProjectsApi.md#get_project) | **GET** /v1/projects/{id} | Get
[**list_project_ssh_keys**](ProjectsApi.md#list_project_ssh_keys) | **GET** /v1/project/{projectId}/ssh-keys | List SSH keys
[**list_projects**](ProjectsApi.md#list_projects) | **GET** /v1/projects | List
[**update_project**](ProjectsApi.md#update_project) | **PATCH** /v1/projects/{project.id} | Update


# **create_project**
> Project create_project(project)

Create

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.ProjectsApi()
project = src.cudo_compute.Project() # Project | 

try:
    # Create
    api_response = api_instance.create_project(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> object delete_project(id)

Delete

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.ProjectsApi()
id = 'id_example' # str | 

try:
    # Delete
    api_response = api_instance.delete_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
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

# **get_project**
> Project get_project(id)

Get

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.ProjectsApi()
id = 'id_example' # str | 

try:
    # Get
    api_response = api_instance.get_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_ssh_keys**
> ListProjectSshKeysResponse list_project_ssh_keys(project_id)

List SSH keys

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.ProjectsApi()
project_id = 'project_id_example' # str | 

try:
    # List SSH keys
    api_response = api_instance.list_project_ssh_keys(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_project_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**ListProjectSshKeysResponse**](ListProjectSshKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ListProjectsResponse list_projects(page_token=page_token, page_size=page_size)

List

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.ProjectsApi()
page_token = 'page_token_example' # str |  (optional)
page_size = 56 # int |  (optional)

try:
    # List
    api_response = api_instance.list_projects(page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_token** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(project_id, update_project_body)

Update

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.ProjectsApi()
project_id = 'project_id_example' # str | 
update_project_body = src.cudo_compute.UpdateProjectBody() # UpdateProjectBody | 

try:
    # Update
    api_response = api_instance.update_project(project_id, update_project_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **update_project_body** | [**UpdateProjectBody**](UpdateProjectBody.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


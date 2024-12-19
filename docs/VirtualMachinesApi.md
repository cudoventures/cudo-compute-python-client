# src.cudo_compute.VirtualMachinesApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_security_group**](VirtualMachinesApi.md#attach_security_group) | **PATCH** /v1/projects/{projectId}/vm/{id}/security-group/attach | Attach security group to VM
[**connect_vm**](VirtualMachinesApi.md#connect_vm) | **GET** /v1/projects/{projectId}/vms/{id}/connect | Connect via VNC
[**count_vms**](VirtualMachinesApi.md#count_vms) | **GET** /v1/projects/{projectId}/count-vms | Count
[**create_private_vm_image**](VirtualMachinesApi.md#create_private_vm_image) | **POST** /v1/projects/{projectId}/images | Create private VM image
[**create_vm**](VirtualMachinesApi.md#create_vm) | **POST** /v1/projects/{projectId}/vm | Create virtual machine
[**delete_private_vm_image**](VirtualMachinesApi.md#delete_private_vm_image) | **DELETE** /v1/projects/{projectId}/images/{id} | Delete private VM image
[**detach_security_group**](VirtualMachinesApi.md#detach_security_group) | **PATCH** /v1/projects/{projectId}/vm/{id}/security-group/detach | Attach security group to VM
[**get_private_vm_image**](VirtualMachinesApi.md#get_private_vm_image) | **GET** /v1/projects/{projectId}/images/{id} | Get private VM image
[**get_vm**](VirtualMachinesApi.md#get_vm) | **GET** /v1/projects/{projectId}/vms/{id} | Get
[**list_private_vm_images**](VirtualMachinesApi.md#list_private_vm_images) | **GET** /v1/projects/{projectId}/images | List private VM images
[**list_public_vm_images**](VirtualMachinesApi.md#list_public_vm_images) | **GET** /v1/vms/public-images | List public VM images
[**list_vm_data_centers**](VirtualMachinesApi.md#list_vm_data_centers) | **GET** /v1/vms/data-centers | List data centers
[**list_vm_disks**](VirtualMachinesApi.md#list_vm_disks) | **GET** /v1/projects/{projectId}/vms/{id}/disks | List disks attached to VM
[**list_vm_gpu_models**](VirtualMachinesApi.md#list_vm_gpu_models) | **GET** /v1/vms/gpu-models | List GPU models
[**list_vm_machine_types2**](VirtualMachinesApi.md#list_vm_machine_types2) | **GET** /v1/vms/machine-types-2 | List machine types v2
[**list_vms**](VirtualMachinesApi.md#list_vms) | **GET** /v1/projects/{projectId}/vms | List
[**monitor_vm**](VirtualMachinesApi.md#monitor_vm) | **GET** /v1/projects/{projectId}/vms/{id}/monitor | Monitor
[**reboot_vm**](VirtualMachinesApi.md#reboot_vm) | **POST** /v1/projects/{projectId}/vms/{id}/reboot | Reboot
[**resize_vm**](VirtualMachinesApi.md#resize_vm) | **POST** /v1/projects/{projectId}/vms/{id}/resize | Resize vCPU and memory of VM
[**resize_vm_disk**](VirtualMachinesApi.md#resize_vm_disk) | **PATCH** /v1/projects/{projectId}/vms/{id}/disks | Resize a VM&#39;s disk
[**start_vm**](VirtualMachinesApi.md#start_vm) | **POST** /v1/projects/{projectId}/vms/{id}/start | Start
[**stop_vm**](VirtualMachinesApi.md#stop_vm) | **POST** /v1/projects/{projectId}/vms/{id}/stop | Stop
[**terminate_vm**](VirtualMachinesApi.md#terminate_vm) | **POST** /v1/projects/{projectId}/vms/{id}/terminate | Terminate
[**update_private_vm_image**](VirtualMachinesApi.md#update_private_vm_image) | **POST** /v1/projects/{projectId}/images/{id} | Update private VM image
[**update_vm_metadata**](VirtualMachinesApi.md#update_vm_metadata) | **POST** /v1/projects/{projectId}/vm/{id}/metadata | Update VM metadata


# **attach_security_group**
> AttachSecurityGroupResponse attach_security_group(project_id, id, security_group_id=security_group_id)

Attach security group to VM

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
security_group_id = 'security_group_id_example' # str |  (optional)

try:
    # Attach security group to VM
    api_response = api_instance.attach_security_group(project_id, id, security_group_id=security_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->attach_security_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **security_group_id** | **str**|  | [optional] 

### Return type

[**AttachSecurityGroupResponse**](AttachSecurityGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_vm**
> ConnectVMResponse connect_vm(project_id, id, connection_id=connection_id)

Connect via VNC

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
connection_id = 'connection_id_example' # str |  (optional)

try:
    # Connect via VNC
    api_response = api_instance.connect_vm(project_id, id, connection_id=connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->connect_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **connection_id** | **str**|  | [optional] 

### Return type

[**ConnectVMResponse**](ConnectVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_vms**
> CountVMsResponse count_vms(project_id)

Count

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 

try:
    # Count
    api_response = api_instance.count_vms(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->count_vms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**CountVMsResponse**](CountVMsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_private_vm_image**
> CreatePrivateVMImageResponse create_private_vm_image(project_id, vm_id, id, description=description)

Create private VM image

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
vm_id = 'vm_id_example' # str | 
id = 'id_example' # str | 
description = 'description_example' # str |  (optional)

try:
    # Create private VM image
    api_response = api_instance.create_private_vm_image(project_id, vm_id, id, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->create_private_vm_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **vm_id** | **str**|  | 
 **id** | **str**|  | 
 **description** | **str**|  | [optional] 

### Return type

[**CreatePrivateVMImageResponse**](CreatePrivateVMImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vm**
> CreateVMResponse create_vm(project_id, create_vm_body)

Create virtual machine

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
create_vm_body = src.cudo_compute.CreateVMBody() # CreateVMBody | 

try:
    # Create virtual machine
    api_response = api_instance.create_vm(project_id, create_vm_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->create_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_vm_body** | [**CreateVMBody**](CreateVMBody.md)|  | 

### Return type

[**CreateVMResponse**](CreateVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_private_vm_image**
> DeletePrivateVMImageResponse delete_private_vm_image(project_id, id)

Delete private VM image

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Delete private VM image
    api_response = api_instance.delete_private_vm_image(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->delete_private_vm_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**DeletePrivateVMImageResponse**](DeletePrivateVMImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_security_group**
> DetachSecurityGroupResponse detach_security_group(project_id, id, security_group_id=security_group_id)

Attach security group to VM

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
security_group_id = 'security_group_id_example' # str |  (optional)

try:
    # Attach security group to VM
    api_response = api_instance.detach_security_group(project_id, id, security_group_id=security_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->detach_security_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **security_group_id** | **str**|  | [optional] 

### Return type

[**DetachSecurityGroupResponse**](DetachSecurityGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_vm_image**
> GetPrivateVMImageResponse get_private_vm_image(project_id, id)

Get private VM image

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Get private VM image
    api_response = api_instance.get_private_vm_image(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->get_private_vm_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GetPrivateVMImageResponse**](GetPrivateVMImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vm**
> GetVMResponse get_vm(project_id, id)

Get

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Get
    api_response = api_instance.get_vm(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->get_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GetVMResponse**](GetVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_private_vm_images**
> ListPrivateVMImagesResponse list_private_vm_images(project_id, page_number=page_number, page_size=page_size)

List private VM images

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # List private VM images
    api_response = api_instance.list_private_vm_images(project_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->list_private_vm_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**ListPrivateVMImagesResponse**](ListPrivateVMImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_vm_images**
> ListPublicVMImagesResponse list_public_vm_images()

List public VM images

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()

try:
    # List public VM images
    api_response = api_instance.list_public_vm_images()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->list_public_vm_images: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListPublicVMImagesResponse**](ListPublicVMImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vm_data_centers**
> ListVMDataCentersResponse list_vm_data_centers(region_id=region_id, renewable_energy=renewable_energy)

List data centers

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
region_id = ['region_id_example'] # list[str] |  (optional)
renewable_energy = true # bool |  (optional)

try:
    # List data centers
    api_response = api_instance.list_vm_data_centers(region_id=region_id, renewable_energy=renewable_energy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->list_vm_data_centers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | [**list[str]**](str.md)|  | [optional] 
 **renewable_energy** | **bool**|  | [optional] 

### Return type

[**ListVMDataCentersResponse**](ListVMDataCentersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vm_disks**
> ListVMDisksResponse list_vm_disks(project_id, id)

List disks attached to VM

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # List disks attached to VM
    api_response = api_instance.list_vm_disks(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->list_vm_disks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**ListVMDisksResponse**](ListVMDisksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vm_gpu_models**
> ListVMGpuModelsResponse list_vm_gpu_models()

List GPU models

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()

try:
    # List GPU models
    api_response = api_instance.list_vm_gpu_models()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->list_vm_gpu_models: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVMGpuModelsResponse**](ListVMGpuModelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vm_machine_types2**
> ListVMMachineTypes2Response list_vm_machine_types2()

List machine types v2

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()

try:
    # List machine types v2
    api_response = api_instance.list_vm_machine_types2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->list_vm_machine_types2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVMMachineTypes2Response**](ListVMMachineTypes2Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vms**
> ListVMsResponse list_vms(project_id, network_id=network_id)

List

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
network_id = 'network_id_example' # str |  (optional)

try:
    # List
    api_response = api_instance.list_vms(project_id, network_id=network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->list_vms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **network_id** | **str**|  | [optional] 

### Return type

[**ListVMsResponse**](ListVMsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_vm**
> MonitorVMResponse monitor_vm(project_id, id)

Monitor

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Monitor
    api_response = api_instance.monitor_vm(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->monitor_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**MonitorVMResponse**](MonitorVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_vm**
> RebootVMResponse reboot_vm(project_id, id)

Reboot

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Reboot
    api_response = api_instance.reboot_vm(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->reboot_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RebootVMResponse**](RebootVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_vm**
> ResizeVMResponse resize_vm(project_id, id, vcpus=vcpus, memory_gib=memory_gib)

Resize vCPU and memory of VM

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
vcpus = 789 # int |  (optional)
memory_gib = 789 # int |  (optional)

try:
    # Resize vCPU and memory of VM
    api_response = api_instance.resize_vm(project_id, id, vcpus=vcpus, memory_gib=memory_gib)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->resize_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **vcpus** | **int**|  | [optional] 
 **memory_gib** | **int**|  | [optional] 

### Return type

[**ResizeVMResponse**](ResizeVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_vm_disk**
> ResizeVMDiskResponse resize_vm_disk(project_id, id, disk_id=disk_id, size_gib=size_gib)

Resize a VM's disk

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
disk_id = 'disk_id_example' # str |  (optional)
size_gib = 56 # int |  (optional)

try:
    # Resize a VM's disk
    api_response = api_instance.resize_vm_disk(project_id, id, disk_id=disk_id, size_gib=size_gib)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->resize_vm_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **disk_id** | **str**|  | [optional] 
 **size_gib** | **int**|  | [optional] 

### Return type

[**ResizeVMDiskResponse**](ResizeVMDiskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_vm**
> StartVMResponse start_vm(project_id, id)

Start

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Start
    api_response = api_instance.start_vm(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->start_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**StartVMResponse**](StartVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_vm**
> StopVMResponse stop_vm(project_id, id)

Stop

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Stop
    api_response = api_instance.stop_vm(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->stop_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**StopVMResponse**](StopVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_vm**
> TerminateVMResponse terminate_vm(project_id, id)

Terminate

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Terminate
    api_response = api_instance.terminate_vm(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->terminate_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**TerminateVMResponse**](TerminateVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_private_vm_image**
> UpdatePrivateVMImageResponse update_private_vm_image(project_id, id, description=description)

Update private VM image

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
description = 'description_example' # str |  (optional)

try:
    # Update private VM image
    api_response = api_instance.update_private_vm_image(project_id, id, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->update_private_vm_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **description** | **str**|  | [optional] 

### Return type

[**UpdatePrivateVMImageResponse**](UpdatePrivateVMImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vm_metadata**
> UpdateVMMetadataResponse update_vm_metadata(project_id, id, update_vm_metadata_body)

Update VM metadata

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.VirtualMachinesApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
update_vm_metadata_body = src.cudo_compute.UpdateVMMetadataBody() # UpdateVMMetadataBody | 

try:
    # Update VM metadata
    api_response = api_instance.update_vm_metadata(project_id, id, update_vm_metadata_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->update_vm_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **update_vm_metadata_body** | [**UpdateVMMetadataBody**](UpdateVMMetadataBody.md)|  | 

### Return type

[**UpdateVMMetadataResponse**](UpdateVMMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


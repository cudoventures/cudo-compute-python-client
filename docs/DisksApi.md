# src.cudo_compute.DisksApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_storage_disk**](DisksApi.md#attach_storage_disk) | **PATCH** /v1/projects/{projectId}/disk/{id}/attach | Attach storage disk to VM
[**create_disk_snapshot**](DisksApi.md#create_disk_snapshot) | **POST** /v1/projects/{projectId}/disks/{id}/snapshots | Create Disk Snapshot
[**create_storage_disk**](DisksApi.md#create_storage_disk) | **POST** /v1/projects/{projectId}/disks | Create storage disk
[**delete_disk_snapshot**](DisksApi.md#delete_disk_snapshot) | **DELETE** /v1/projects/{projectId}/disks/{id}/snapshots | Delete Disk Snapshots
[**delete_storage_disk**](DisksApi.md#delete_storage_disk) | **DELETE** /v1/projects/{projectId}/disks/{id} | Delete storage disk
[**detach_storage_disk**](DisksApi.md#detach_storage_disk) | **PUT** /v1/projects/{projectId}/disk/{id}/detach | Detach storage disk from VM
[**get_disk**](DisksApi.md#get_disk) | **GET** /v1/projects/{projectId}/disks/{id} | List disks
[**list_disk_snapshots**](DisksApi.md#list_disk_snapshots) | **GET** /v1/projects/{projectId}/disks/{id}/snapshots | List Disk Snapshots
[**list_disks**](DisksApi.md#list_disks) | **GET** /v1/projects/{projectId}/disks | List disks
[**revert_disk**](DisksApi.md#revert_disk) | **POST** /v1/projects/{projectId}/disks/{id}/revert | Revert Disk to Snapshot


# **attach_storage_disk**
> AttachStorageDiskResponse attach_storage_disk(project_id, id, vm_id=vm_id)

Attach storage disk to VM

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DisksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
vm_id = 'vm_id_example' # str |  (optional)

try:
    # Attach storage disk to VM
    api_response = api_instance.attach_storage_disk(project_id, id, vm_id=vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->attach_storage_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **vm_id** | **str**|  | [optional] 

### Return type

[**AttachStorageDiskResponse**](AttachStorageDiskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_disk_snapshot**
> CreateDiskSnapshotResponse create_disk_snapshot(project_id, id, create_disk_snapshot_body)

Create Disk Snapshot

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DisksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
create_disk_snapshot_body = src.cudo_compute.CreateDiskSnapshotBody() # CreateDiskSnapshotBody | 

try:
    # Create Disk Snapshot
    api_response = api_instance.create_disk_snapshot(project_id, id, create_disk_snapshot_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->create_disk_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **create_disk_snapshot_body** | [**CreateDiskSnapshotBody**](CreateDiskSnapshotBody.md)|  | 

### Return type

[**CreateDiskSnapshotResponse**](CreateDiskSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_storage_disk**
> CreateStorageDiskResponse create_storage_disk(project_id, create_storage_disk_body)

Create storage disk

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DisksApi()
project_id = 'project_id_example' # str | 
create_storage_disk_body = src.cudo_compute.CreateStorageDiskBody() # CreateStorageDiskBody | 

try:
    # Create storage disk
    api_response = api_instance.create_storage_disk(project_id, create_storage_disk_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->create_storage_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_storage_disk_body** | [**CreateStorageDiskBody**](CreateStorageDiskBody.md)|  | 

### Return type

[**CreateStorageDiskResponse**](CreateStorageDiskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_disk_snapshot**
> DeleteDiskSnapshotResponse delete_disk_snapshot(project_id, id, snapshot_id, vm_id)

Delete Disk Snapshots

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DisksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
snapshot_id = 'snapshot_id_example' # str | 
vm_id = 'vm_id_example' # str | 

try:
    # Delete Disk Snapshots
    api_response = api_instance.delete_disk_snapshot(project_id, id, snapshot_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->delete_disk_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **snapshot_id** | **str**|  | 
 **vm_id** | **str**|  | 

### Return type

[**DeleteDiskSnapshotResponse**](DeleteDiskSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage_disk**
> DeleteStorageDiskResponse delete_storage_disk(project_id, id)

Delete storage disk

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DisksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Delete storage disk
    api_response = api_instance.delete_storage_disk(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->delete_storage_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**DeleteStorageDiskResponse**](DeleteStorageDiskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_storage_disk**
> DetachStorageDiskResponse detach_storage_disk(project_id, id)

Detach storage disk from VM

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DisksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # Detach storage disk from VM
    api_response = api_instance.detach_storage_disk(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->detach_storage_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**DetachStorageDiskResponse**](DetachStorageDiskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk**
> GetDiskResponse get_disk(project_id, id)

List disks

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DisksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # List disks
    api_response = api_instance.get_disk(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->get_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GetDiskResponse**](GetDiskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_disk_snapshots**
> ListDiskSnapshotsResponse list_disk_snapshots(project_id, id)

List Disk Snapshots

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DisksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    # List Disk Snapshots
    api_response = api_instance.list_disk_snapshots(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->list_disk_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**ListDiskSnapshotsResponse**](ListDiskSnapshotsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_disks**
> ListDisksResponse list_disks(project_id, page_number=page_number, page_size=page_size, data_center_id=data_center_id)

List disks

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DisksApi()
project_id = 'project_id_example' # str | 
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
data_center_id = 'data_center_id_example' # str |  (optional)

try:
    # List disks
    api_response = api_instance.list_disks(project_id, page_number=page_number, page_size=page_size, data_center_id=data_center_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->list_disks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **data_center_id** | **str**|  | [optional] 

### Return type

[**ListDisksResponse**](ListDisksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_disk**
> RevertDiskResponse revert_disk(project_id, id, snapshot_id, vm_id)

Revert Disk to Snapshot

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DisksApi()
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 
snapshot_id = 'snapshot_id_example' # str | 
vm_id = 'vm_id_example' # str | 

try:
    # Revert Disk to Snapshot
    api_response = api_instance.revert_disk(project_id, id, snapshot_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->revert_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 
 **snapshot_id** | **str**|  | 
 **vm_id** | **str**|  | 

### Return type

[**RevertDiskResponse**](RevertDiskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


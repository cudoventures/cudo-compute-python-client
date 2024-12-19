# src.cudo_compute.DataCentersApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_hosts**](DataCentersApi.md#count_hosts) | **GET** /v1/data-centers/{dataCenterId}/host-count | Get host count
[**create_data_center**](DataCentersApi.md#create_data_center) | **POST** /v1/data-centers | Create data center
[**delete_data_center**](DataCentersApi.md#delete_data_center) | **DELETE** /v1/data-centers/{id} | Delete data center
[**get_data_center**](DataCentersApi.md#get_data_center) | **GET** /v1/data-centers/{id} | Get data center
[**get_data_center_live_utilization**](DataCentersApi.md#get_data_center_live_utilization) | **GET** /v1/data-centers/{id}/live-utilization | Get live utilization
[**get_data_center_revenue_by_resource**](DataCentersApi.md#get_data_center_revenue_by_resource) | **GET** /v1/data-centers/{id}/revenue-by-resource | Get revenue by resource
[**get_data_center_revenue_time_series**](DataCentersApi.md#get_data_center_revenue_time_series) | **GET** /v1/data-centers/{id}/revenue | Get revenue time series
[**list_clusters**](DataCentersApi.md#list_clusters) | **GET** /v1/data-centers/{dataCenterId}/clusters | List clusters
[**list_data_centers**](DataCentersApi.md#list_data_centers) | **GET** /v1/data-centers | List data centers
[**list_hosts**](DataCentersApi.md#list_hosts) | **GET** /v1/data-centers/{dataCenterId}/hosts | List hosts
[**update_data_center**](DataCentersApi.md#update_data_center) | **PATCH** /v1/data-centers/{dataCenter.id} | Update data center


# **count_hosts**
> CountHostsResponse count_hosts(data_center_id)

Get host count

Returns the number of hosts in a data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
data_center_id = 'data_center_id_example' # str | 

try:
    # Get host count
    api_response = api_instance.count_hosts(data_center_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->count_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 

### Return type

[**CountHostsResponse**](CountHostsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_center**
> V1DataCenter create_data_center(data_center)

Create data center

Creates a new data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
data_center = src.cudo_compute.V1DataCenter() # V1DataCenter | 

try:
    # Create data center
    api_response = api_instance.create_data_center(data_center)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->create_data_center: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center** | [**V1DataCenter**](V1DataCenter.md)|  | 

### Return type

[**V1DataCenter**](V1DataCenter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_center**
> object delete_data_center(id)

Delete data center

Deletes a data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
id = 'id_example' # str | 

try:
    # Delete data center
    api_response = api_instance.delete_data_center(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->delete_data_center: %s\n" % e)
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

# **get_data_center**
> V1DataCenter get_data_center(id)

Get data center

Returns a data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
id = 'id_example' # str | 

try:
    # Get data center
    api_response = api_instance.get_data_center(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->get_data_center: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1DataCenter**](V1DataCenter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_center_live_utilization**
> GetDataCenterLiveUtilizationResponse get_data_center_live_utilization(id)

Get live utilization

Returns the live utilization of a data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
id = 'id_example' # str | 

try:
    # Get live utilization
    api_response = api_instance.get_data_center_live_utilization(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->get_data_center_live_utilization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetDataCenterLiveUtilizationResponse**](GetDataCenterLiveUtilizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_center_revenue_by_resource**
> GetDataCenterRevenueByResourceResponse get_data_center_revenue_by_resource(id, start_time, end_time)

Get revenue by resource

Returns the revenue of a data center by resource (CPU, Memory, Storage, etc.)

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
id = 'id_example' # str | 
start_time = '2013-10-20T19:20:30+01:00' # datetime | 
end_time = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    # Get revenue by resource
    api_response = api_instance.get_data_center_revenue_by_resource(id, start_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->get_data_center_revenue_by_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **start_time** | **datetime**|  | 
 **end_time** | **datetime**|  | 

### Return type

[**GetDataCenterRevenueByResourceResponse**](GetDataCenterRevenueByResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_center_revenue_time_series**
> GetDataCenterRevenueTimeSeriesResponse get_data_center_revenue_time_series(id, start_time, end_time, interval)

Get revenue time series

Returns the revenue of a data center over time

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
id = 'id_example' # str | 
start_time = '2013-10-20T19:20:30+01:00' # datetime | 
end_time = '2013-10-20T19:20:30+01:00' # datetime | 
interval = 'INTERVAL_UNKNOWN' # str |  (default to INTERVAL_UNKNOWN)

try:
    # Get revenue time series
    api_response = api_instance.get_data_center_revenue_time_series(id, start_time, end_time, interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->get_data_center_revenue_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **start_time** | **datetime**|  | 
 **end_time** | **datetime**|  | 
 **interval** | **str**|  | [default to INTERVAL_UNKNOWN]

### Return type

[**GetDataCenterRevenueTimeSeriesResponse**](GetDataCenterRevenueTimeSeriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clusters**
> ListClustersResponse list_clusters(data_center_id)

List clusters

Returns the clusters in a data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
data_center_id = 'data_center_id_example' # str | 

try:
    # List clusters
    api_response = api_instance.list_clusters(data_center_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->list_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 

### Return type

[**ListClustersResponse**](ListClustersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_centers**
> ListDataCentersResponse list_data_centers(page_token=page_token, page_size=page_size)

List data centers

Returns the data centers in an organization

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
page_token = 'page_token_example' # str |  (optional)
page_size = 56 # int |  (optional)

try:
    # List data centers
    api_response = api_instance.list_data_centers(page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->list_data_centers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_token** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**ListDataCentersResponse**](ListDataCentersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hosts**
> ListHostsResponse list_hosts(data_center_id)

List hosts

Returns the hosts in a data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
data_center_id = 'data_center_id_example' # str | 

try:
    # List hosts
    api_response = api_instance.list_hosts(data_center_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->list_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 

### Return type

[**ListHostsResponse**](ListHostsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_center**
> V1DataCenter update_data_center(data_center_id, update_data_center_body)

Update data center

Updates a data center

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.DataCentersApi()
data_center_id = 'data_center_id_example' # str | 
update_data_center_body = src.cudo_compute.UpdateDataCenterBody() # UpdateDataCenterBody | 

try:
    # Update data center
    api_response = api_instance.update_data_center(data_center_id, update_data_center_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCentersApi->update_data_center: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_center_id** | **str**|  | 
 **update_data_center_body** | [**UpdateDataCenterBody**](UpdateDataCenterBody.md)|  | 

### Return type

[**V1DataCenter**](V1DataCenter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


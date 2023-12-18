# src.cudo_compute.BillingApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_account**](BillingApi.md#create_billing_account) | **POST** /v1/billing-accounts | Create a billing account
[**delete_billing_account**](BillingApi.md#delete_billing_account) | **DELETE** /v1/billing-accounts/{id} | Delete billing account
[**get_billing_account**](BillingApi.md#get_billing_account) | **GET** /v1/billing-accounts/{id} | Get a billing account
[**get_billing_account_details**](BillingApi.md#get_billing_account_details) | **GET** /v1/billing-accounts/{id}/details | Get billing account details
[**get_billing_account_payment_methods**](BillingApi.md#get_billing_account_payment_methods) | **GET** /v1/billing-accounts/{id}/payment-methods | Get payment methods
[**get_billing_account_setup_intent**](BillingApi.md#get_billing_account_setup_intent) | **GET** /v1/billing-accounts/{id}/setup-intent | Get setup intent
[**get_billing_account_spend_details**](BillingApi.md#get_billing_account_spend_details) | **GET** /v1/billing-accounts/{billingAccountId}/spend/details | Get spend details
[**get_billing_account_stripe_invoices**](BillingApi.md#get_billing_account_stripe_invoices) | **GET** /v1/billing-accounts/invoices | Get invoices
[**list_billing_accounts**](BillingApi.md#list_billing_accounts) | **GET** /v1/billing-accounts | List billing accounts
[**list_outstanding_stripe_invoices**](BillingApi.md#list_outstanding_stripe_invoices) | **GET** /v1/billing-accounts/invoices/outstanding | Get outstanding invoices
[**remove_billing_account_payment_method**](BillingApi.md#remove_billing_account_payment_method) | **DELETE** /v1/billing-accounts/{id}/payment-methods/{paymentMethodId} | Remove payment method
[**set_billing_account_default_payment_method**](BillingApi.md#set_billing_account_default_payment_method) | **POST** /v1/billing-accounts/{id}/payment-methods/{paymentMethodId}/set-default | Set default payment method
[**update_billing_account**](BillingApi.md#update_billing_account) | **PATCH** /v1/billing-accounts/{billingAccount.id} | Update billing account


# **create_billing_account**
> BillingAccount create_billing_account(create_billing_account_body)

Create a billing account

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
create_billing_account_body = src.cudo_compute.CreateBillingAccountRequest() # CreateBillingAccountRequest | 

try:
    # Create a billing account
    api_response = api_instance.create_billing_account(create_billing_account_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->create_billing_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_billing_account_body** | [**CreateBillingAccountRequest**](CreateBillingAccountRequest.md)|  | 

### Return type

[**BillingAccount**](BillingAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_account**
> object delete_billing_account(id)

Delete billing account

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
id = 'id_example' # str | 

try:
    # Delete billing account
    api_response = api_instance.delete_billing_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->delete_billing_account: %s\n" % e)
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

# **get_billing_account**
> BillingAccount get_billing_account(id)

Get a billing account

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
id = 'id_example' # str | 

try:
    # Get a billing account
    api_response = api_instance.get_billing_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BillingAccount**](BillingAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_account_details**
> GetBillingAccountDetailsResponse get_billing_account_details(id)

Get billing account details

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
id = 'id_example' # str | 

try:
    # Get billing account details
    api_response = api_instance.get_billing_account_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_account_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetBillingAccountDetailsResponse**](GetBillingAccountDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_account_payment_methods**
> BillingAccountPaymentMethods get_billing_account_payment_methods(id)

Get payment methods

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
id = 'id_example' # str | 

try:
    # Get payment methods
    api_response = api_instance.get_billing_account_payment_methods(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_account_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BillingAccountPaymentMethods**](BillingAccountPaymentMethods.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_account_setup_intent**
> BillingAccountSetupIntent get_billing_account_setup_intent(id)

Get setup intent

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
id = 'id_example' # str | 

try:
    # Get setup intent
    api_response = api_instance.get_billing_account_setup_intent(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_account_setup_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BillingAccountSetupIntent**](BillingAccountSetupIntent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_account_spend_details**
> GetBillingAccountSpendDetailsResponse get_billing_account_spend_details(billing_account_id, start_time, end_time)

Get spend details

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
billing_account_id = 'billing_account_id_example' # str | 
start_time = '2013-10-20T19:20:30+01:00' # datetime | 
end_time = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    # Get spend details
    api_response = api_instance.get_billing_account_spend_details(billing_account_id, start_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_account_spend_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_account_id** | **str**|  | 
 **start_time** | **datetime**|  | 
 **end_time** | **datetime**|  | 

### Return type

[**GetBillingAccountSpendDetailsResponse**](GetBillingAccountSpendDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_account_stripe_invoices**
> GetBillingAccountStripeInvoicesResponse get_billing_account_stripe_invoices(id, page_size=page_size, starting_after=starting_after, status=status)

Get invoices

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
id = 'id_example' # str | 
page_size = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
status = 'status_example' # str |  (optional)

try:
    # Get invoices
    api_response = api_instance.get_billing_account_stripe_invoices(id, page_size=page_size, starting_after=starting_after, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_billing_account_stripe_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page_size** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**GetBillingAccountStripeInvoicesResponse**](GetBillingAccountStripeInvoicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_billing_accounts**
> ListBillingAccountsResponse list_billing_accounts(page_token=page_token, page_size=page_size)

List billing accounts

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
page_token = 'page_token_example' # str |  (optional)
page_size = 56 # int |  (optional)

try:
    # List billing accounts
    api_response = api_instance.list_billing_accounts(page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_billing_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_token** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**ListBillingAccountsResponse**](ListBillingAccountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_outstanding_stripe_invoices**
> ListOutstandingStripeInvoicesResponse list_outstanding_stripe_invoices()

Get outstanding invoices

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()

try:
    # Get outstanding invoices
    api_response = api_instance.list_outstanding_stripe_invoices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_outstanding_stripe_invoices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListOutstandingStripeInvoicesResponse**](ListOutstandingStripeInvoicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_billing_account_payment_method**
> RemoveBillingAccountPaymentMethodResponse remove_billing_account_payment_method(id, payment_method_id)

Remove payment method

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
id = 'id_example' # str | 
payment_method_id = 'payment_method_id_example' # str | 

try:
    # Remove payment method
    api_response = api_instance.remove_billing_account_payment_method(id, payment_method_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->remove_billing_account_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **payment_method_id** | **str**|  | 

### Return type

[**RemoveBillingAccountPaymentMethodResponse**](RemoveBillingAccountPaymentMethodResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_billing_account_default_payment_method**
> SetBillingAccountDefaultPaymentMethodResponse set_billing_account_default_payment_method(id, payment_method_id)

Set default payment method

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
id = 'id_example' # str | 
payment_method_id = 'payment_method_id_example' # str | 

try:
    # Set default payment method
    api_response = api_instance.set_billing_account_default_payment_method(id, payment_method_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->set_billing_account_default_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **payment_method_id** | **str**|  | 

### Return type

[**SetBillingAccountDefaultPaymentMethodResponse**](SetBillingAccountDefaultPaymentMethodResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_account**
> BillingAccount update_billing_account(billing_account_id, update_billing_account_body)

Update billing account

### Example
```python
from __future__ import print_function
import time
import src.cudo_compute
from src.cudo_compute.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = src.cudo_compute.BillingApi()
billing_account_id = 'billing_account_id_example' # str | 
update_billing_account_body = src.cudo_compute.UpdateBillingAccountBody() # UpdateBillingAccountBody | 

try:
    # Update billing account
    api_response = api_instance.update_billing_account(billing_account_id, update_billing_account_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->update_billing_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_account_id** | **str**|  | 
 **update_billing_account_body** | [**UpdateBillingAccountBody**](UpdateBillingAccountBody.md)|  | 

### Return type

[**BillingAccount**](BillingAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


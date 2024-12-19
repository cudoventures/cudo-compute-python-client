# src.cudo_compute.BillingApi

All URIs are relative to *https://rest.compute.cudo.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_account**](BillingApi.md#create_billing_account) | **POST** /v1/billing-accounts | Create a billing account
[**create_billing_account_credit_payment**](BillingApi.md#create_billing_account_credit_payment) | **POST** /v1/billing-accounts/{id}/credit | Add credit to billing account
[**delete_billing_account**](BillingApi.md#delete_billing_account) | **DELETE** /v1/billing-accounts/{id} | Delete billing account
[**get_billing_account**](BillingApi.md#get_billing_account) | **GET** /v1/billing-accounts/{id} | Get a billing account
[**get_billing_account_details**](BillingApi.md#get_billing_account_details) | **GET** /v1/billing-accounts/{id}/details | Get billing account details
[**get_billing_account_payment_methods**](BillingApi.md#get_billing_account_payment_methods) | **GET** /v1/billing-accounts/{id}/payment-methods | Get payment methods
[**get_billing_account_setup_intent**](BillingApi.md#get_billing_account_setup_intent) | **GET** /v1/billing-accounts/{id}/setup-intent | Get setup intent
[**get_billing_account_spend_details**](BillingApi.md#get_billing_account_spend_details) | **GET** /v1/billing-accounts/{billingAccountId}/spend/details | Get spend details
[**list_billing_account_credit_balance_transactions**](BillingApi.md#list_billing_account_credit_balance_transactions) | **GET** /v1/billing-accounts/{id}/credit-balance-transactions | List credit balance transactions on a billing account
[**list_billing_account_invoices**](BillingApi.md#list_billing_account_invoices) | **GET** /v1/billing-accounts/invoices | List invoices
[**list_billing_account_transactions**](BillingApi.md#list_billing_account_transactions) | **GET** /v1/billing-accounts/{id}/transactions | List transactions on a billing account
[**list_billing_accounts**](BillingApi.md#list_billing_accounts) | **GET** /v1/billing-accounts | List billing accounts
[**list_outstanding_invoices**](BillingApi.md#list_outstanding_invoices) | **GET** /v1/billing-accounts/invoices/outstanding | Get outstanding invoices
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

# **create_billing_account_credit_payment**
> CreateBillingAccountCreditPaymentResponse create_billing_account_credit_payment(id, payment_method, amount_value=amount_value, radar_session_id=radar_session_id)

Add credit to billing account

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
payment_method = 'payment_method_example' # str | 
amount_value = 'amount_value_example' # str | The decimal value, as a string.  The string representation consists of an optional sign, `+` (`U+002B`) or `-` (`U+002D`), followed by a sequence of zero or more decimal digits (\"the integer\"), optionally followed by a fraction, optionally followed by an exponent.  The fraction consists of a decimal point followed by zero or more decimal digits. The string must contain at least one digit in either the integer or the fraction. The number formed by the sign, the integer and the fraction is referred to as the significand.  The exponent consists of the character `e` (`U+0065`) or `E` (`U+0045`) followed by one or more decimal digits.  Services **should** normalize decimal values before storing them by:    - Removing an explicitly-provided `+` sign (`+2.5` -> `2.5`).   - Replacing a zero-length integer value with `0` (`.5` -> `0.5`).   - Coercing the exponent character to lower-case (`2.5E8` -> `2.5e8`).   - Removing an explicitly-provided zero exponent (`2.5e0` -> `2.5`).  Services **may** perform additional normalization based on its own needs and the internal decimal implementation selected, such as shifting the decimal point and exponent value together (example: `2.5e-1` <-> `0.25`). Additionally, services **may** preserve trailing zeroes in the fraction to indicate increased precision, but are not required to do so.  Note that only the `.` character is supported to divide the integer and the fraction; `,` **should not** be supported regardless of locale. Additionally, thousand separators **should not** be supported. If a service does support them, values **must** be normalized.  The ENBF grammar is:      DecimalString =       [Sign] Significand [Exponent];      Sign = '+' | '-';      Significand =       Digits ['.'] [Digits] | [Digits] '.' Digits;      Exponent = ('e' | 'E') [Sign] Digits;      Digits = { '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' };  Services **should** clearly document the range of supported values, the maximum supported precision (total number of digits), and, if applicable, the scale (number of digits after the decimal point), as well as how it behaves when receiving out-of-bounds values.  Services **may** choose to accept values passed as input even when the value has a higher precision or scale than the service supports, and **should** round the value to fit the supported scale. Alternatively, the service **may** error with `400 Bad Request` (`INVALID_ARGUMENT` in gRPC) if precision would be lost.  Services **should** error with `400 Bad Request` (`INVALID_ARGUMENT` in gRPC) if the service receives a value outside of the supported range. (optional)
radar_session_id = 'radar_session_id_example' # str |  (optional)

try:
    # Add credit to billing account
    api_response = api_instance.create_billing_account_credit_payment(id, payment_method, amount_value=amount_value, radar_session_id=radar_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->create_billing_account_credit_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **payment_method** | **str**|  | 
 **amount_value** | **str**| The decimal value, as a string.  The string representation consists of an optional sign, &#x60;+&#x60; (&#x60;U+002B&#x60;) or &#x60;-&#x60; (&#x60;U+002D&#x60;), followed by a sequence of zero or more decimal digits (\&quot;the integer\&quot;), optionally followed by a fraction, optionally followed by an exponent.  The fraction consists of a decimal point followed by zero or more decimal digits. The string must contain at least one digit in either the integer or the fraction. The number formed by the sign, the integer and the fraction is referred to as the significand.  The exponent consists of the character &#x60;e&#x60; (&#x60;U+0065&#x60;) or &#x60;E&#x60; (&#x60;U+0045&#x60;) followed by one or more decimal digits.  Services **should** normalize decimal values before storing them by:    - Removing an explicitly-provided &#x60;+&#x60; sign (&#x60;+2.5&#x60; -&gt; &#x60;2.5&#x60;).   - Replacing a zero-length integer value with &#x60;0&#x60; (&#x60;.5&#x60; -&gt; &#x60;0.5&#x60;).   - Coercing the exponent character to lower-case (&#x60;2.5E8&#x60; -&gt; &#x60;2.5e8&#x60;).   - Removing an explicitly-provided zero exponent (&#x60;2.5e0&#x60; -&gt; &#x60;2.5&#x60;).  Services **may** perform additional normalization based on its own needs and the internal decimal implementation selected, such as shifting the decimal point and exponent value together (example: &#x60;2.5e-1&#x60; &lt;-&gt; &#x60;0.25&#x60;). Additionally, services **may** preserve trailing zeroes in the fraction to indicate increased precision, but are not required to do so.  Note that only the &#x60;.&#x60; character is supported to divide the integer and the fraction; &#x60;,&#x60; **should not** be supported regardless of locale. Additionally, thousand separators **should not** be supported. If a service does support them, values **must** be normalized.  The ENBF grammar is:      DecimalString &#x3D;       [Sign] Significand [Exponent];      Sign &#x3D; &#39;+&#39; | &#39;-&#39;;      Significand &#x3D;       Digits [&#39;.&#39;] [Digits] | [Digits] &#39;.&#39; Digits;      Exponent &#x3D; (&#39;e&#39; | &#39;E&#39;) [Sign] Digits;      Digits &#x3D; { &#39;0&#39; | &#39;1&#39; | &#39;2&#39; | &#39;3&#39; | &#39;4&#39; | &#39;5&#39; | &#39;6&#39; | &#39;7&#39; | &#39;8&#39; | &#39;9&#39; };  Services **should** clearly document the range of supported values, the maximum supported precision (total number of digits), and, if applicable, the scale (number of digits after the decimal point), as well as how it behaves when receiving out-of-bounds values.  Services **may** choose to accept values passed as input even when the value has a higher precision or scale than the service supports, and **should** round the value to fit the supported scale. Alternatively, the service **may** error with &#x60;400 Bad Request&#x60; (&#x60;INVALID_ARGUMENT&#x60; in gRPC) if precision would be lost.  Services **should** error with &#x60;400 Bad Request&#x60; (&#x60;INVALID_ARGUMENT&#x60; in gRPC) if the service receives a value outside of the supported range. | [optional] 
 **radar_session_id** | **str**|  | [optional] 

### Return type

[**CreateBillingAccountCreditPaymentResponse**](CreateBillingAccountCreditPaymentResponse.md)

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

# **list_billing_account_credit_balance_transactions**
> ListBillingAccountCreditBalanceTransactionsResponse list_billing_account_credit_balance_transactions(id, page_size=page_size, starting_after=starting_after)

List credit balance transactions on a billing account

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

try:
    # List credit balance transactions on a billing account
    api_response = api_instance.list_billing_account_credit_balance_transactions(id, page_size=page_size, starting_after=starting_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_billing_account_credit_balance_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page_size** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 

### Return type

[**ListBillingAccountCreditBalanceTransactionsResponse**](ListBillingAccountCreditBalanceTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_billing_account_invoices**
> ListBillingAccountInvoicesResponse list_billing_account_invoices(id, page_size=page_size, starting_after=starting_after, status=status)

List invoices

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
    # List invoices
    api_response = api_instance.list_billing_account_invoices(id, page_size=page_size, starting_after=starting_after, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_billing_account_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page_size** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**ListBillingAccountInvoicesResponse**](ListBillingAccountInvoicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_billing_account_transactions**
> ListBillingAccountTransactionsResponse list_billing_account_transactions(id, page_size=page_size, starting_after=starting_after)

List transactions on a billing account

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

try:
    # List transactions on a billing account
    api_response = api_instance.list_billing_account_transactions(id, page_size=page_size, starting_after=starting_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_billing_account_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page_size** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 

### Return type

[**ListBillingAccountTransactionsResponse**](ListBillingAccountTransactionsResponse.md)

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

# **list_outstanding_invoices**
> ListOutstandingInvoicesResponse list_outstanding_invoices()

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
    api_response = api_instance.list_outstanding_invoices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_outstanding_invoices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListOutstandingInvoicesResponse**](ListOutstandingInvoicesResponse.md)

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


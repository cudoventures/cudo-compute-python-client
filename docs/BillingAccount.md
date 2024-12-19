# BillingAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**create_time** | **datetime** |  | [optional] 
**display_name** | **str** |  | [optional] 
**stripe_ref** | **str** |  | [optional] 
**create_by** | **str** |  | [optional] 
**monthly_spend** | **str** |  | [optional] 
**hourly_spend_rate** | [**Decimal**](Decimal.md) |  | [optional] 
**tax_id** | [**TaxId**](TaxId.md) |  | [optional] 
**invoice_time** | **datetime** |  | [optional] 
**billing_threshold** | [**Decimal**](Decimal.md) |  | [optional] 
**monthly_spend_limit** | [**Decimal**](Decimal.md) |  | [optional] 
**hourly_spend_limit** | [**Decimal**](Decimal.md) |  | [optional] 
**next_invoice_total** | [**Decimal**](Decimal.md) |  | [optional] 
**credit_balance** | [**Decimal**](Decimal.md) |  | [optional] 
**credit_balance_recharge** | [**CreditBalanceRecharge**](CreditBalanceRecharge.md) |  | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**state** | [**BillingAccountState**](BillingAccountState.md) |  | [optional] 
**payment_terms** | [**PaymentTerms**](PaymentTerms.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



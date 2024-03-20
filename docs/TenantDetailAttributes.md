# TenantDetailAttributes

The type specific properties of the tenants object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_prefix** | **str** | The domain prefix of the tenant | 
**display_name** | **str** | Display name used within Auvik | [optional] 
**tenant_type** | **str** | The type of tenant in Auvik. A finite list of enumerated string values | 
**enabled** | **bool** | Whether or not the tenant is enabled | 
**subscribed** | **bool** | Whether or not the tenant is subscribed | 
**subscription_owner** | **str** | The owner who subscribes the tenant | 
**running** | **bool** | Whether or not the tenant is running | 
**trial_start_date** | **str** | Start date of trial | [optional] 
**trial_end_date** | **str** | Start date of trial | [optional] 
**address** | [**TenantDetailAttributesAddress**](TenantDetailAttributesAddress.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenant_detail_attributes import TenantDetailAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDetailAttributes from a JSON string
tenant_detail_attributes_instance = TenantDetailAttributes.from_json(json)
# print the JSON string representation of the object
print TenantDetailAttributes.to_json()

# convert the object into a dict
tenant_detail_attributes_dict = tenant_detail_attributes_instance.to_dict()
# create an instance of TenantDetailAttributes from a dict
tenant_detail_attributes_form_dict = tenant_detail_attributes.from_dict(tenant_detail_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



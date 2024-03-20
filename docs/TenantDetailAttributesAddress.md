# TenantDetailAttributesAddress

Address of the tenant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Tenant&#39;s mailing address | [optional] 
**address2** | **str** | Additional address information | [optional] 
**city** | **str** | City tenant is located in | [optional] 
**state_province** | **str** | State or region tenant is located in | [optional] 
**zip_postal_code** | **str** | Zip code or postal code of tenant&#39;s mailing address | [optional] 
**state** | **str** | State or region tenant is located in | [optional] 
**postal_code** | **str** | Zip code or postal code of tenant&#39;s mailing address | [optional] 
**country** | **str** | Country tenant is located in | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenant_detail_attributes_address import TenantDetailAttributesAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDetailAttributesAddress from a JSON string
tenant_detail_attributes_address_instance = TenantDetailAttributesAddress.from_json(json)
# print the JSON string representation of the object
print TenantDetailAttributesAddress.to_json()

# convert the object into a dict
tenant_detail_attributes_address_dict = tenant_detail_attributes_address_instance.to_dict()
# create an instance of TenantDetailAttributesAddress from a dict
tenant_detail_attributes_address_form_dict = tenant_detail_attributes_address.from_dict(tenant_detail_attributes_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



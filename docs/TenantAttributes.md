# TenantAttributes

The type specific properties of the tenants object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_prefix** | **str** | The domain prefix of the tenant | 
**tenant_type** | **str** | The type of tenant in Auvik. A finite list of enumerated string values | 

## Example

```python
from layer8_auvik_api_client.models.tenant_attributes import TenantAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAttributes from a JSON string
tenant_attributes_instance = TenantAttributes.from_json(json)
# print the JSON string representation of the object
print TenantAttributes.to_json()

# convert the object into a dict
tenant_attributes_dict = tenant_attributes_instance.to_dict()
# create an instance of TenantAttributes from a dict
tenant_attributes_form_dict = tenant_attributes.from_dict(tenant_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



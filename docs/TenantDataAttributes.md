# TenantDataAttributes

The type-specific properties of the tenant object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_prefix** | **str** | The domain prefix of the tenant | 

## Example

```python
from layer8_auvik_api_client.models.tenant_data_attributes import TenantDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDataAttributes from a JSON string
tenant_data_attributes_instance = TenantDataAttributes.from_json(json)
# print the JSON string representation of the object
print TenantDataAttributes.to_json()

# convert the object into a dict
tenant_data_attributes_dict = tenant_data_attributes_instance.to_dict()
# create an instance of TenantDataAttributes from a dict
tenant_data_attributes_form_dict = tenant_data_attributes.from_dict(tenant_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



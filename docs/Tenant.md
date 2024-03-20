# Tenant

This entity's owning tenant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TenantData**](TenantData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenant import Tenant

# TODO update the JSON string below
json = "{}"
# create an instance of Tenant from a JSON string
tenant_instance = Tenant.from_json(json)
# print the JSON string representation of the object
print Tenant.to_json()

# convert the object into a dict
tenant_dict = tenant_instance.to_dict()
# create an instance of Tenant from a dict
tenant_form_dict = tenant.from_dict(tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



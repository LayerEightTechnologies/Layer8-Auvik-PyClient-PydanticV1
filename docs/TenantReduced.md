# TenantReduced

This entity's owning tenant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TenantReducedData**](TenantReducedData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenant_reduced import TenantReduced

# TODO update the JSON string below
json = "{}"
# create an instance of TenantReduced from a JSON string
tenant_reduced_instance = TenantReduced.from_json(json)
# print the JSON string representation of the object
print TenantReduced.to_json()

# convert the object into a dict
tenant_reduced_dict = tenant_reduced_instance.to_dict()
# create an instance of TenantReduced from a dict
tenant_reduced_form_dict = tenant_reduced.from_dict(tenant_reduced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



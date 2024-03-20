# TenantReducedData

The template for a resource object representing an Auvik tenant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API. | [optional] 
**id** | **str** | The unique identifier for a tenant | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenant_reduced_data import TenantReducedData

# TODO update the JSON string below
json = "{}"
# create an instance of TenantReducedData from a JSON string
tenant_reduced_data_instance = TenantReducedData.from_json(json)
# print the JSON string representation of the object
print TenantReducedData.to_json()

# convert the object into a dict
tenant_reduced_data_dict = tenant_reduced_data_instance.to_dict()
# create an instance of TenantReducedData from a dict
tenant_reduced_data_form_dict = tenant_reduced_data.from_dict(tenant_reduced_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



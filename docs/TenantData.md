# TenantData

The template for a resource object representing an Auvik tenant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API. | [optional] 
**id** | **str** | The unique identifier for a tenant | [optional] 
**attributes** | [**TenantDataAttributes**](TenantDataAttributes.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenant_data import TenantData

# TODO update the JSON string below
json = "{}"
# create an instance of TenantData from a JSON string
tenant_data_instance = TenantData.from_json(json)
# print the JSON string representation of the object
print TenantData.to_json()

# convert the object into a dict
tenant_data_dict = tenant_data_instance.to_dict()
# create an instance of TenantData from a dict
tenant_data_form_dict = tenant_data.from_dict(tenant_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



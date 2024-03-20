# TenantsResourceObject

The template for a resource object representing an Auvik tenant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API. | [optional] 
**id** | **str** | The unique identifier for a tenant | [optional] 
**attributes** | [**TenantAttributes**](TenantAttributes.md) |  | [optional] 
**relationships** | [**TenantsResourceObjectRelationships**](TenantsResourceObjectRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenants_resource_object import TenantsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of TenantsResourceObject from a JSON string
tenants_resource_object_instance = TenantsResourceObject.from_json(json)
# print the JSON string representation of the object
print TenantsResourceObject.to_json()

# convert the object into a dict
tenants_resource_object_dict = tenants_resource_object_instance.to_dict()
# create an instance of TenantsResourceObject from a dict
tenants_resource_object_form_dict = tenants_resource_object.from_dict(tenants_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TenantsResourceObjectRelationshipsParentData

The parent tenant data object of the tenant selected

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API. | [optional] 
**id** | **str** | The unique identifier for a tenant | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenants_resource_object_relationships_parent_data import TenantsResourceObjectRelationshipsParentData

# TODO update the JSON string below
json = "{}"
# create an instance of TenantsResourceObjectRelationshipsParentData from a JSON string
tenants_resource_object_relationships_parent_data_instance = TenantsResourceObjectRelationshipsParentData.from_json(json)
# print the JSON string representation of the object
print TenantsResourceObjectRelationshipsParentData.to_json()

# convert the object into a dict
tenants_resource_object_relationships_parent_data_dict = tenants_resource_object_relationships_parent_data_instance.to_dict()
# create an instance of TenantsResourceObjectRelationshipsParentData from a dict
tenants_resource_object_relationships_parent_data_form_dict = tenants_resource_object_relationships_parent_data.from_dict(tenants_resource_object_relationships_parent_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



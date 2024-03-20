# TenantsResourceObjectRelationships

The type specific relationship of the tenants object to other entities

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**TenantsResourceObjectRelationshipsParent**](TenantsResourceObjectRelationshipsParent.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenants_resource_object_relationships import TenantsResourceObjectRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TenantsResourceObjectRelationships from a JSON string
tenants_resource_object_relationships_instance = TenantsResourceObjectRelationships.from_json(json)
# print the JSON string representation of the object
print TenantsResourceObjectRelationships.to_json()

# convert the object into a dict
tenants_resource_object_relationships_dict = tenants_resource_object_relationships_instance.to_dict()
# create an instance of TenantsResourceObjectRelationships from a dict
tenants_resource_object_relationships_form_dict = tenants_resource_object_relationships.from_dict(tenants_resource_object_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



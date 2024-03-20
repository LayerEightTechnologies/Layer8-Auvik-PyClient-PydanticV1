# TenantDetailResourceObjectRelationshipsParent

The parent tenant container object of the tenant selected

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TenantDetailResourceObjectRelationshipsParentData**](TenantDetailResourceObjectRelationshipsParentData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenant_detail_resource_object_relationships_parent import TenantDetailResourceObjectRelationshipsParent

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDetailResourceObjectRelationshipsParent from a JSON string
tenant_detail_resource_object_relationships_parent_instance = TenantDetailResourceObjectRelationshipsParent.from_json(json)
# print the JSON string representation of the object
print TenantDetailResourceObjectRelationshipsParent.to_json()

# convert the object into a dict
tenant_detail_resource_object_relationships_parent_dict = tenant_detail_resource_object_relationships_parent_instance.to_dict()
# create an instance of TenantDetailResourceObjectRelationshipsParent from a dict
tenant_detail_resource_object_relationships_parent_form_dict = tenant_detail_resource_object_relationships_parent.from_dict(tenant_detail_resource_object_relationships_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



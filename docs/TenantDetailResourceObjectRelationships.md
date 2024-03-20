# TenantDetailResourceObjectRelationships

The type specific relationship of the legacy tenants object to other entities

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**TenantDetailResourceObjectRelationshipsParent**](TenantDetailResourceObjectRelationshipsParent.md) |  | [optional] 
**authorizations** | [**TenantDetailResourceObjectRelationshipsAuthorizations**](TenantDetailResourceObjectRelationshipsAuthorizations.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenant_detail_resource_object_relationships import TenantDetailResourceObjectRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDetailResourceObjectRelationships from a JSON string
tenant_detail_resource_object_relationships_instance = TenantDetailResourceObjectRelationships.from_json(json)
# print the JSON string representation of the object
print TenantDetailResourceObjectRelationships.to_json()

# convert the object into a dict
tenant_detail_resource_object_relationships_dict = tenant_detail_resource_object_relationships_instance.to_dict()
# create an instance of TenantDetailResourceObjectRelationships from a dict
tenant_detail_resource_object_relationships_form_dict = tenant_detail_resource_object_relationships.from_dict(tenant_detail_resource_object_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



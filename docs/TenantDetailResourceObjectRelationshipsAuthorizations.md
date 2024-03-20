# TenantDetailResourceObjectRelationshipsAuthorizations

The The authorization container object of the tenant selected

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TenantDetailResourceObjectRelationshipsAuthorizationsData]**](TenantDetailResourceObjectRelationshipsAuthorizationsData.md) | The list of authorization to the tenant selected | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenant_detail_resource_object_relationships_authorizations import TenantDetailResourceObjectRelationshipsAuthorizations

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDetailResourceObjectRelationshipsAuthorizations from a JSON string
tenant_detail_resource_object_relationships_authorizations_instance = TenantDetailResourceObjectRelationshipsAuthorizations.from_json(json)
# print the JSON string representation of the object
print TenantDetailResourceObjectRelationshipsAuthorizations.to_json()

# convert the object into a dict
tenant_detail_resource_object_relationships_authorizations_dict = tenant_detail_resource_object_relationships_authorizations_instance.to_dict()
# create an instance of TenantDetailResourceObjectRelationshipsAuthorizations from a dict
tenant_detail_resource_object_relationships_authorizations_form_dict = tenant_detail_resource_object_relationships_authorizations.from_dict(tenant_detail_resource_object_relationships_authorizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



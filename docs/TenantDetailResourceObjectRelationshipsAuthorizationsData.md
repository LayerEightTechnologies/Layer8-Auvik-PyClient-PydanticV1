# TenantDetailResourceObjectRelationshipsAuthorizationsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of authorizations | [optional] 
**id** | **str** | The id is granted for authorization | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenant_detail_resource_object_relationships_authorizations_data import TenantDetailResourceObjectRelationshipsAuthorizationsData

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDetailResourceObjectRelationshipsAuthorizationsData from a JSON string
tenant_detail_resource_object_relationships_authorizations_data_instance = TenantDetailResourceObjectRelationshipsAuthorizationsData.from_json(json)
# print the JSON string representation of the object
print TenantDetailResourceObjectRelationshipsAuthorizationsData.to_json()

# convert the object into a dict
tenant_detail_resource_object_relationships_authorizations_data_dict = tenant_detail_resource_object_relationships_authorizations_data_instance.to_dict()
# create an instance of TenantDetailResourceObjectRelationshipsAuthorizationsData from a dict
tenant_detail_resource_object_relationships_authorizations_data_form_dict = tenant_detail_resource_object_relationships_authorizations_data.from_dict(tenant_detail_resource_object_relationships_authorizations_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



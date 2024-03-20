# OidRelationships

This OID's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**device** | [**OidRelationshipsDevice**](OidRelationshipsDevice.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.oid_relationships import OidRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of OidRelationships from a JSON string
oid_relationships_instance = OidRelationships.from_json(json)
# print the JSON string representation of the object
print OidRelationships.to_json()

# convert the object into a dict
oid_relationships_dict = oid_relationships_instance.to_dict()
# create an instance of OidRelationships from a dict
oid_relationships_form_dict = oid_relationships.from_dict(oid_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



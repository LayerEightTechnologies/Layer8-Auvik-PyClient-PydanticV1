# AuditRelationships

This entity audit's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**device** | [**AuditRelationshipsDevice**](AuditRelationshipsDevice.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.audit_relationships import AuditRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AuditRelationships from a JSON string
audit_relationships_instance = AuditRelationships.from_json(json)
# print the JSON string representation of the object
print AuditRelationships.to_json()

# convert the object into a dict
audit_relationships_dict = audit_relationships_instance.to_dict()
# create an instance of AuditRelationships from a dict
audit_relationships_form_dict = audit_relationships.from_dict(audit_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



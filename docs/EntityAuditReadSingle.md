# EntityAuditReadSingle

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuditsResourceObject**](AuditsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.entity_audit_read_single import EntityAuditReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAuditReadSingle from a JSON string
entity_audit_read_single_instance = EntityAuditReadSingle.from_json(json)
# print the JSON string representation of the object
print EntityAuditReadSingle.to_json()

# convert the object into a dict
entity_audit_read_single_dict = entity_audit_read_single_instance.to_dict()
# create an instance of EntityAuditReadSingle from a dict
entity_audit_read_single_form_dict = entity_audit_read_single.from_dict(entity_audit_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



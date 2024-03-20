# AuditRelationshipsDevice

This device associated with this audit log

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuditRelationshipsDeviceData**](AuditRelationshipsDeviceData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.audit_relationships_device import AuditRelationshipsDevice

# TODO update the JSON string below
json = "{}"
# create an instance of AuditRelationshipsDevice from a JSON string
audit_relationships_device_instance = AuditRelationshipsDevice.from_json(json)
# print the JSON string representation of the object
print AuditRelationshipsDevice.to_json()

# convert the object into a dict
audit_relationships_device_dict = audit_relationships_device_instance.to_dict()
# create an instance of AuditRelationshipsDevice from a dict
audit_relationships_device_form_dict = audit_relationships_device.from_dict(audit_relationships_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



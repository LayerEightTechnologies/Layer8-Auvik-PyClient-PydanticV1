# AuditRelationshipsDeviceData

A device resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API. | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**attributes** | [**AuditRelationshipsDeviceDataAttributes**](AuditRelationshipsDeviceDataAttributes.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.audit_relationships_device_data import AuditRelationshipsDeviceData

# TODO update the JSON string below
json = "{}"
# create an instance of AuditRelationshipsDeviceData from a JSON string
audit_relationships_device_data_instance = AuditRelationshipsDeviceData.from_json(json)
# print the JSON string representation of the object
print AuditRelationshipsDeviceData.to_json()

# convert the object into a dict
audit_relationships_device_data_dict = audit_relationships_device_data_instance.to_dict()
# create an instance of AuditRelationshipsDeviceData from a dict
audit_relationships_device_data_form_dict = audit_relationships_device_data.from_dict(audit_relationships_device_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AuditRelationshipsDeviceDataAttributes

The type-specific properties of the device object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device&#39;s name | [optional] 

## Example

```python
from layer8_auvik_api_client.models.audit_relationships_device_data_attributes import AuditRelationshipsDeviceDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AuditRelationshipsDeviceDataAttributes from a JSON string
audit_relationships_device_data_attributes_instance = AuditRelationshipsDeviceDataAttributes.from_json(json)
# print the JSON string representation of the object
print AuditRelationshipsDeviceDataAttributes.to_json()

# convert the object into a dict
audit_relationships_device_data_attributes_dict = audit_relationships_device_data_attributes_instance.to_dict()
# create an instance of AuditRelationshipsDeviceDataAttributes from a dict
audit_relationships_device_data_attributes_form_dict = audit_relationships_device_data_attributes.from_dict(audit_relationships_device_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



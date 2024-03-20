# InterfaceRelationshipsParentDevice

This interface's parent device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InterfaceRelationshipsParentDeviceData**](InterfaceRelationshipsParentDeviceData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_relationships_parent_device import InterfaceRelationshipsParentDevice

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRelationshipsParentDevice from a JSON string
interface_relationships_parent_device_instance = InterfaceRelationshipsParentDevice.from_json(json)
# print the JSON string representation of the object
print InterfaceRelationshipsParentDevice.to_json()

# convert the object into a dict
interface_relationships_parent_device_dict = interface_relationships_parent_device_instance.to_dict()
# create an instance of InterfaceRelationshipsParentDevice from a dict
interface_relationships_parent_device_form_dict = interface_relationships_parent_device.from_dict(interface_relationships_parent_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



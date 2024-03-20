# InterfaceRelationshipsParentDeviceData

A device resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This device&#39;s ID | [optional] 
**type** | **str** | The type of the object | [optional] 
**links** | [**InterfaceRelationshipsParentDeviceDataLinks**](InterfaceRelationshipsParentDeviceDataLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_relationships_parent_device_data import InterfaceRelationshipsParentDeviceData

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRelationshipsParentDeviceData from a JSON string
interface_relationships_parent_device_data_instance = InterfaceRelationshipsParentDeviceData.from_json(json)
# print the JSON string representation of the object
print InterfaceRelationshipsParentDeviceData.to_json()

# convert the object into a dict
interface_relationships_parent_device_data_dict = interface_relationships_parent_device_data_instance.to_dict()
# create an instance of InterfaceRelationshipsParentDeviceData from a dict
interface_relationships_parent_device_data_form_dict = interface_relationships_parent_device_data.from_dict(interface_relationships_parent_device_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



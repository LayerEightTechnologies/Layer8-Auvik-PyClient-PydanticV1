# InterfaceRelationshipsParentDeviceDataLinks

Links relating to this device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this device&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this set of device info | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_relationships_parent_device_data_links import InterfaceRelationshipsParentDeviceDataLinks

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRelationshipsParentDeviceDataLinks from a JSON string
interface_relationships_parent_device_data_links_instance = InterfaceRelationshipsParentDeviceDataLinks.from_json(json)
# print the JSON string representation of the object
print InterfaceRelationshipsParentDeviceDataLinks.to_json()

# convert the object into a dict
interface_relationships_parent_device_data_links_dict = interface_relationships_parent_device_data_links_instance.to_dict()
# create an instance of InterfaceRelationshipsParentDeviceDataLinks from a dict
interface_relationships_parent_device_data_links_form_dict = interface_relationships_parent_device_data_links.from_dict(interface_relationships_parent_device_data_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



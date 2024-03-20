# DeviceDetailsRelationshipsConnectedDevicesLinks

Links relating to this connected device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this connected device&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this connected device | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_connected_devices_links import DeviceDetailsRelationshipsConnectedDevicesLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsConnectedDevicesLinks from a JSON string
device_details_relationships_connected_devices_links_instance = DeviceDetailsRelationshipsConnectedDevicesLinks.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsConnectedDevicesLinks.to_json()

# convert the object into a dict
device_details_relationships_connected_devices_links_dict = device_details_relationships_connected_devices_links_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsConnectedDevicesLinks from a dict
device_details_relationships_connected_devices_links_form_dict = device_details_relationships_connected_devices_links.from_dict(device_details_relationships_connected_devices_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



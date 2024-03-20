# DeviceDetailsRelationshipsConnectedDevices

List of other devices connected to this device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeviceDetailsRelationshipsConnectedDevicesData]**](DeviceDetailsRelationshipsConnectedDevicesData.md) | A connected device resource object | 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_connected_devices import DeviceDetailsRelationshipsConnectedDevices

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsConnectedDevices from a JSON string
device_details_relationships_connected_devices_instance = DeviceDetailsRelationshipsConnectedDevices.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsConnectedDevices.to_json()

# convert the object into a dict
device_details_relationships_connected_devices_dict = device_details_relationships_connected_devices_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsConnectedDevices from a dict
device_details_relationships_connected_devices_form_dict = device_details_relationships_connected_devices.from_dict(device_details_relationships_connected_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



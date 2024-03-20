# DeviceDetailsRelationshipsConnectedDevicesData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Connected device&#39;s ID | [optional] 
**attributes** | [**DeviceDetailsRelationshipsConnectedDevicesAttributes**](DeviceDetailsRelationshipsConnectedDevicesAttributes.md) |  | [optional] 
**type** | **str** | The type of object in the API | [optional] 
**links** | [**DeviceDetailsRelationshipsConnectedDevicesLinks**](DeviceDetailsRelationshipsConnectedDevicesLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_connected_devices_data import DeviceDetailsRelationshipsConnectedDevicesData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsConnectedDevicesData from a JSON string
device_details_relationships_connected_devices_data_instance = DeviceDetailsRelationshipsConnectedDevicesData.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsConnectedDevicesData.to_json()

# convert the object into a dict
device_details_relationships_connected_devices_data_dict = device_details_relationships_connected_devices_data_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsConnectedDevicesData from a dict
device_details_relationships_connected_devices_data_form_dict = device_details_relationships_connected_devices_data.from_dict(device_details_relationships_connected_devices_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



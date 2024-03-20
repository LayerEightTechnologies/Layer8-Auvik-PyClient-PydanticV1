# DeviceDetailsRelationshipsConnectedDevicesAttributes

The type-specific properties of the connected device object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Connected device&#39;s name | 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_connected_devices_attributes import DeviceDetailsRelationshipsConnectedDevicesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsConnectedDevicesAttributes from a JSON string
device_details_relationships_connected_devices_attributes_instance = DeviceDetailsRelationshipsConnectedDevicesAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsConnectedDevicesAttributes.to_json()

# convert the object into a dict
device_details_relationships_connected_devices_attributes_dict = device_details_relationships_connected_devices_attributes_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsConnectedDevicesAttributes from a dict
device_details_relationships_connected_devices_attributes_form_dict = device_details_relationships_connected_devices_attributes.from_dict(device_details_relationships_connected_devices_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



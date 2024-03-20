# DeviceExtendedDetailsDevice

The template for a resource object representing an Auvik device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**links** | [**DeviceExtendedDetailsDeviceLinks**](DeviceExtendedDetailsDeviceLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_extended_details_device import DeviceExtendedDetailsDevice

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceExtendedDetailsDevice from a JSON string
device_extended_details_device_instance = DeviceExtendedDetailsDevice.from_json(json)
# print the JSON string representation of the object
print DeviceExtendedDetailsDevice.to_json()

# convert the object into a dict
device_extended_details_device_dict = device_extended_details_device_instance.to_dict()
# create an instance of DeviceExtendedDetailsDevice from a dict
device_extended_details_device_form_dict = device_extended_details_device.from_dict(device_extended_details_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



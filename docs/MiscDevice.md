# MiscDevice

Extended details for a miscellaneous device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**links** | [**DeviceExtendedDetailsDeviceLinks**](DeviceExtendedDetailsDeviceLinks.md) |  | [optional] 
**attributes** | [**MiscDeviceAllOfAttributes**](MiscDeviceAllOfAttributes.md) |  | [optional] 
**relationships** | [**DeviceRelationships**](DeviceRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.misc_device import MiscDevice

# TODO update the JSON string below
json = "{}"
# create an instance of MiscDevice from a JSON string
misc_device_instance = MiscDevice.from_json(json)
# print the JSON string representation of the object
print MiscDevice.to_json()

# convert the object into a dict
misc_device_dict = misc_device_instance.to_dict()
# create an instance of MiscDevice from a dict
misc_device_form_dict = misc_device.from_dict(misc_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



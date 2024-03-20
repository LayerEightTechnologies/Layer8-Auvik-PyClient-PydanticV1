# DeviceExtendedDetailResourceObject


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
from layer8_auvik_api_client.models.device_extended_detail_resource_object import DeviceExtendedDetailResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceExtendedDetailResourceObject from a JSON string
device_extended_detail_resource_object_instance = DeviceExtendedDetailResourceObject.from_json(json)
# print the JSON string representation of the object
print DeviceExtendedDetailResourceObject.to_json()

# convert the object into a dict
device_extended_detail_resource_object_dict = device_extended_detail_resource_object_instance.to_dict()
# create an instance of DeviceExtendedDetailResourceObject from a dict
device_extended_detail_resource_object_form_dict = device_extended_detail_resource_object.from_dict(device_extended_detail_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



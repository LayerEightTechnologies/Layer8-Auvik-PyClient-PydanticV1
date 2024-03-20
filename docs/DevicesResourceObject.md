# DevicesResourceObject

The template for a resource object representing an Auvik device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**attributes** | [**DeviceAttributes**](DeviceAttributes.md) |  | [optional] 
**relationships** | [**DeviceRelationships**](DeviceRelationships.md) |  | [optional] 
**links** | [**DevicesResourceObjectLinks**](DevicesResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.devices_resource_object import DevicesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesResourceObject from a JSON string
devices_resource_object_instance = DevicesResourceObject.from_json(json)
# print the JSON string representation of the object
print DevicesResourceObject.to_json()

# convert the object into a dict
devices_resource_object_dict = devices_resource_object_instance.to_dict()
# create an instance of DevicesResourceObject from a dict
devices_resource_object_form_dict = devices_resource_object.from_dict(devices_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



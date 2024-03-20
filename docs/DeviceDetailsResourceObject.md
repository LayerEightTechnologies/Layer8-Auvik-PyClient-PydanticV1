# DeviceDetailsResourceObject

The template for a resource object representing an Auvik device's extra details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**attributes** | [**DeviceDetailsAttributes**](DeviceDetailsAttributes.md) |  | [optional] 
**relationships** | [**DeviceDetailsRelationships**](DeviceDetailsRelationships.md) |  | [optional] 
**links** | [**DeviceDetailsResourceObjectLinks**](DeviceDetailsResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_resource_object import DeviceDetailsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsResourceObject from a JSON string
device_details_resource_object_instance = DeviceDetailsResourceObject.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsResourceObject.to_json()

# convert the object into a dict
device_details_resource_object_dict = device_details_resource_object_instance.to_dict()
# create an instance of DeviceDetailsResourceObject from a dict
device_details_resource_object_form_dict = device_details_resource_object.from_dict(device_details_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



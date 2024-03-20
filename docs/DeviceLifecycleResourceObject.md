# DeviceLifecycleResourceObject

The template for a resource object representing an Auvik device with lifecycle information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**attributes** | [**DeviceLifecycleAttributes**](DeviceLifecycleAttributes.md) |  | [optional] 
**relationships** | [**DeviceLifecycleRelationships**](DeviceLifecycleRelationships.md) |  | [optional] 
**links** | [**DeviceLifecycleResourceObjectLinks**](DeviceLifecycleResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_lifecycle_resource_object import DeviceLifecycleResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLifecycleResourceObject from a JSON string
device_lifecycle_resource_object_instance = DeviceLifecycleResourceObject.from_json(json)
# print the JSON string representation of the object
print DeviceLifecycleResourceObject.to_json()

# convert the object into a dict
device_lifecycle_resource_object_dict = device_lifecycle_resource_object_instance.to_dict()
# create an instance of DeviceLifecycleResourceObject from a dict
device_lifecycle_resource_object_form_dict = device_lifecycle_resource_object.from_dict(device_lifecycle_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



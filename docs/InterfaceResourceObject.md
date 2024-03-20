# InterfaceResourceObject

The template for a resource object representing an interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a interface | [optional] 
**attributes** | [**InterfaceAttributes**](InterfaceAttributes.md) |  | [optional] 
**links** | [**InterfaceResourceObjectLinks**](InterfaceResourceObjectLinks.md) |  | [optional] 
**relationships** | [**InterfaceRelationships**](InterfaceRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_resource_object import InterfaceResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceResourceObject from a JSON string
interface_resource_object_instance = InterfaceResourceObject.from_json(json)
# print the JSON string representation of the object
print InterfaceResourceObject.to_json()

# convert the object into a dict
interface_resource_object_dict = interface_resource_object_instance.to_dict()
# create an instance of InterfaceResourceObject from a dict
interface_resource_object_form_dict = interface_resource_object.from_dict(interface_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ConfigResourceObject

The template for a resource object representing an Auvik device's configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a configuration | [optional] 
**attributes** | [**ConfigAttributes**](ConfigAttributes.md) |  | [optional] 
**relationships** | [**ConfigRelationships**](ConfigRelationships.md) |  | [optional] 
**links** | [**ConfigResourceObjectLinks**](ConfigResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.config_resource_object import ConfigResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigResourceObject from a JSON string
config_resource_object_instance = ConfigResourceObject.from_json(json)
# print the JSON string representation of the object
print ConfigResourceObject.to_json()

# convert the object into a dict
config_resource_object_dict = config_resource_object_instance.to_dict()
# create an instance of ConfigResourceObject from a dict
config_resource_object_form_dict = config_resource_object.from_dict(config_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



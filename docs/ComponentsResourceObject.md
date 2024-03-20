# ComponentsResourceObject

The template for a resource object representing an Auvik component

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for this component | [optional] 
**attributes** | [**ComponentAttributes**](ComponentAttributes.md) |  | [optional] 
**links** | [**ComponentsResourceObjectLinks**](ComponentsResourceObjectLinks.md) |  | [optional] 
**relationships** | [**ComponentRelationships**](ComponentRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.components_resource_object import ComponentsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentsResourceObject from a JSON string
components_resource_object_instance = ComponentsResourceObject.from_json(json)
# print the JSON string representation of the object
print ComponentsResourceObject.to_json()

# convert the object into a dict
components_resource_object_dict = components_resource_object_instance.to_dict()
# create an instance of ComponentsResourceObject from a dict
components_resource_object_form_dict = components_resource_object.from_dict(components_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



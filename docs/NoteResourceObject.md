# NoteResourceObject

The template for a resource object representing an Auvik note

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for this note | [optional] 
**attributes** | [**NoteAttributes**](NoteAttributes.md) |  | [optional] 
**relationships** | [**NoteRelationships**](NoteRelationships.md) |  | [optional] 
**links** | [**NoteResourceObjectLinks**](NoteResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.note_resource_object import NoteResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of NoteResourceObject from a JSON string
note_resource_object_instance = NoteResourceObject.from_json(json)
# print the JSON string representation of the object
print NoteResourceObject.to_json()

# convert the object into a dict
note_resource_object_dict = note_resource_object_instance.to_dict()
# create an instance of NoteResourceObject from a dict
note_resource_object_form_dict = note_resource_object.from_dict(note_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



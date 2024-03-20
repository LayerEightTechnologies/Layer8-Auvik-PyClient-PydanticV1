# NoteAttributes

The type-specific properties of the notes object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | This note&#39;s title | 
**body** | **str** | Content of this note | 
**entity_id** | **str** | The related entity&#39;s ID | 
**entity_type** | **str** | The related entity type | 
**entity_name** | **str** | The related entity&#39;s name | 
**last_modified_by** | **str** | The username that last modified the note | 
**last_modified** | **str** | When one of this entity note&#39;s attributes was last modified | 

## Example

```python
from layer8_auvik_api_client.models.note_attributes import NoteAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NoteAttributes from a JSON string
note_attributes_instance = NoteAttributes.from_json(json)
# print the JSON string representation of the object
print NoteAttributes.to_json()

# convert the object into a dict
note_attributes_dict = note_attributes_instance.to_dict()
# create an instance of NoteAttributes from a dict
note_attributes_form_dict = note_attributes.from_dict(note_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



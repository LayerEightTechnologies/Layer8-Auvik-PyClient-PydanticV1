# EntityNotesReadMultiple

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NoteResourceObject]**](NoteResourceObject.md) |  | [optional] 
**links** | [**EntityNotesReadMultipleLinks**](EntityNotesReadMultipleLinks.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.entity_notes_read_multiple import EntityNotesReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of EntityNotesReadMultiple from a JSON string
entity_notes_read_multiple_instance = EntityNotesReadMultiple.from_json(json)
# print the JSON string representation of the object
print EntityNotesReadMultiple.to_json()

# convert the object into a dict
entity_notes_read_multiple_dict = entity_notes_read_multiple_instance.to_dict()
# create an instance of EntityNotesReadMultiple from a dict
entity_notes_read_multiple_form_dict = entity_notes_read_multiple.from_dict(entity_notes_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



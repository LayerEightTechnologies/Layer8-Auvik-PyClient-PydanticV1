# NoteRelationships

This entity note's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.note_relationships import NoteRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of NoteRelationships from a JSON string
note_relationships_instance = NoteRelationships.from_json(json)
# print the JSON string representation of the object
print NoteRelationships.to_json()

# convert the object into a dict
note_relationships_dict = note_relationships_instance.to_dict()
# create an instance of NoteRelationships from a dict
note_relationships_form_dict = note_relationships.from_dict(note_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



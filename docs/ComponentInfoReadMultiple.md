# ComponentInfoReadMultiple

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ComponentsResourceObject]**](ComponentsResourceObject.md) |  | [optional] 
**links** | [**ComponentInfoReadMultipleLinks**](ComponentInfoReadMultipleLinks.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_info_read_multiple import ComponentInfoReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentInfoReadMultiple from a JSON string
component_info_read_multiple_instance = ComponentInfoReadMultiple.from_json(json)
# print the JSON string representation of the object
print ComponentInfoReadMultiple.to_json()

# convert the object into a dict
component_info_read_multiple_dict = component_info_read_multiple_instance.to_dict()
# create an instance of ComponentInfoReadMultiple from a dict
component_info_read_multiple_form_dict = component_info_read_multiple.from_dict(component_info_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



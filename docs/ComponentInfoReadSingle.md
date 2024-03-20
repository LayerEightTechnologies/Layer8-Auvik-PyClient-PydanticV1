# ComponentInfoReadSingle

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ComponentsResourceObject**](ComponentsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_info_read_single import ComponentInfoReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentInfoReadSingle from a JSON string
component_info_read_single_instance = ComponentInfoReadSingle.from_json(json)
# print the JSON string representation of the object
print ComponentInfoReadSingle.to_json()

# convert the object into a dict
component_info_read_single_dict = component_info_read_single_instance.to_dict()
# create an instance of ComponentInfoReadSingle from a dict
component_info_read_single_form_dict = component_info_read_single.from_dict(component_info_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



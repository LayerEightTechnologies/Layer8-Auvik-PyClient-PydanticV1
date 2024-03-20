# ConfigReadMultiple

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConfigResourceObject]**](ConfigResourceObject.md) |  | [optional] 
**links** | [**ConfigReadMultipleLinks**](ConfigReadMultipleLinks.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.config_read_multiple import ConfigReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigReadMultiple from a JSON string
config_read_multiple_instance = ConfigReadMultiple.from_json(json)
# print the JSON string representation of the object
print ConfigReadMultiple.to_json()

# convert the object into a dict
config_read_multiple_dict = config_read_multiple_instance.to_dict()
# create an instance of ConfigReadMultiple from a dict
config_read_multiple_form_dict = config_read_multiple.from_dict(config_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ConfigReadSingle

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ConfigResourceObject**](ConfigResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.config_read_single import ConfigReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigReadSingle from a JSON string
config_read_single_instance = ConfigReadSingle.from_json(json)
# print the JSON string representation of the object
print ConfigReadSingle.to_json()

# convert the object into a dict
config_read_single_dict = config_read_single_instance.to_dict()
# create an instance of ConfigReadSingle from a dict
config_read_single_form_dict = config_read_single.from_dict(config_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



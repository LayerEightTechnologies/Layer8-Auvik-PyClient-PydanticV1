# InterfaceInfoReadMultiple

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InterfaceResourceObject]**](InterfaceResourceObject.md) |  | [optional] 
**links** | [**InterfaceInfoReadMultipleLinks**](InterfaceInfoReadMultipleLinks.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_info_read_multiple import InterfaceInfoReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceInfoReadMultiple from a JSON string
interface_info_read_multiple_instance = InterfaceInfoReadMultiple.from_json(json)
# print the JSON string representation of the object
print InterfaceInfoReadMultiple.to_json()

# convert the object into a dict
interface_info_read_multiple_dict = interface_info_read_multiple_instance.to_dict()
# create an instance of InterfaceInfoReadMultiple from a dict
interface_info_read_multiple_form_dict = interface_info_read_multiple.from_dict(interface_info_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InterfaceInfoReadSingle

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InterfaceResourceObject**](InterfaceResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_info_read_single import InterfaceInfoReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceInfoReadSingle from a JSON string
interface_info_read_single_instance = InterfaceInfoReadSingle.from_json(json)
# print the JSON string representation of the object
print InterfaceInfoReadSingle.to_json()

# convert the object into a dict
interface_info_read_single_dict = interface_info_read_single_instance.to_dict()
# create an instance of InterfaceInfoReadSingle from a dict
interface_info_read_single_form_dict = interface_info_read_single.from_dict(interface_info_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



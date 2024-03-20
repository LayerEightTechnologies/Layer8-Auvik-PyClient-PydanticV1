# InterfaceStatisticsRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InterfaceStatisticsResourceObject**](InterfaceStatisticsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_statistics_read import InterfaceStatisticsRead

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStatisticsRead from a JSON string
interface_statistics_read_instance = InterfaceStatisticsRead.from_json(json)
# print the JSON string representation of the object
print InterfaceStatisticsRead.to_json()

# convert the object into a dict
interface_statistics_read_dict = interface_statistics_read_instance.to_dict()
# create an instance of InterfaceStatisticsRead from a dict
interface_statistics_read_form_dict = interface_statistics_read.from_dict(interface_statistics_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



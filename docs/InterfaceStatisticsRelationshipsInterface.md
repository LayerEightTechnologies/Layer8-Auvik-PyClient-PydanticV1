# InterfaceStatisticsRelationshipsInterface

This interface the statistics are reported against

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InterfaceStatisticsRelationshipsInterfaceData**](InterfaceStatisticsRelationshipsInterfaceData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_statistics_relationships_interface import InterfaceStatisticsRelationshipsInterface

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStatisticsRelationshipsInterface from a JSON string
interface_statistics_relationships_interface_instance = InterfaceStatisticsRelationshipsInterface.from_json(json)
# print the JSON string representation of the object
print InterfaceStatisticsRelationshipsInterface.to_json()

# convert the object into a dict
interface_statistics_relationships_interface_dict = interface_statistics_relationships_interface_instance.to_dict()
# create an instance of InterfaceStatisticsRelationshipsInterface from a dict
interface_statistics_relationships_interface_form_dict = interface_statistics_relationships_interface.from_dict(interface_statistics_relationships_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



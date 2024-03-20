# InterfaceStatisticsRelationshipsInterfaceData

A interface resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This interface&#39;s ID | [optional] 
**type** | **str** | The type of the object | [optional] 
**interface_name** | **str** | This interface&#39;s name | [optional] 
**interface_type** | **str** | This interface&#39;s type | [optional] 
**parent_device** | **str** | This interface&#39;s parent device | [optional] 
**links** | [**InterfaceStatisticsRelationshipsInterfaceDataLinks**](InterfaceStatisticsRelationshipsInterfaceDataLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_statistics_relationships_interface_data import InterfaceStatisticsRelationshipsInterfaceData

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStatisticsRelationshipsInterfaceData from a JSON string
interface_statistics_relationships_interface_data_instance = InterfaceStatisticsRelationshipsInterfaceData.from_json(json)
# print the JSON string representation of the object
print InterfaceStatisticsRelationshipsInterfaceData.to_json()

# convert the object into a dict
interface_statistics_relationships_interface_data_dict = interface_statistics_relationships_interface_data_instance.to_dict()
# create an instance of InterfaceStatisticsRelationshipsInterfaceData from a dict
interface_statistics_relationships_interface_data_form_dict = interface_statistics_relationships_interface_data.from_dict(interface_statistics_relationships_interface_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



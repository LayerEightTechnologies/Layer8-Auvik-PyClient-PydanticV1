# InterfaceStatisticsRelationshipsInterfaceDataLinks

Links relating to this interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this interfaces&#39;s dashboard in Auvik | [optional] 
**parent_device** | **str** | Link to this interfaces&#39;s parent device dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this set of interface info | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_statistics_relationships_interface_data_links import InterfaceStatisticsRelationshipsInterfaceDataLinks

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStatisticsRelationshipsInterfaceDataLinks from a JSON string
interface_statistics_relationships_interface_data_links_instance = InterfaceStatisticsRelationshipsInterfaceDataLinks.from_json(json)
# print the JSON string representation of the object
print InterfaceStatisticsRelationshipsInterfaceDataLinks.to_json()

# convert the object into a dict
interface_statistics_relationships_interface_data_links_dict = interface_statistics_relationships_interface_data_links_instance.to_dict()
# create an instance of InterfaceStatisticsRelationshipsInterfaceDataLinks from a dict
interface_statistics_relationships_interface_data_links_form_dict = interface_statistics_relationships_interface_data_links.from_dict(interface_statistics_relationships_interface_data_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



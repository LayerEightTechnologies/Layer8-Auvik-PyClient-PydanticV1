# InterfaceStatisticsResourceObjectLinks

Links relating to this interface statistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this interface&#39;s record in the Interface Info API | [optional] 
**var_self** | **str** | Link used to get this result set | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_statistics_resource_object_links import InterfaceStatisticsResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStatisticsResourceObjectLinks from a JSON string
interface_statistics_resource_object_links_instance = InterfaceStatisticsResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print InterfaceStatisticsResourceObjectLinks.to_json()

# convert the object into a dict
interface_statistics_resource_object_links_dict = interface_statistics_resource_object_links_instance.to_dict()
# create an instance of InterfaceStatisticsResourceObjectLinks from a dict
interface_statistics_resource_object_links_form_dict = interface_statistics_resource_object_links.from_dict(interface_statistics_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



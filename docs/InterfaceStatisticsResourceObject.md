# InterfaceStatisticsResourceObject

Interface statistics resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID for this statistic | [optional] 
**type** | **str** | The type of this resource object | [optional] 
**attributes** | [**StatisticsAttributes**](StatisticsAttributes.md) |  | [optional] 
**relationships** | [**InterfaceStatisticsRelationships**](InterfaceStatisticsRelationships.md) |  | [optional] 
**links** | [**InterfaceStatisticsResourceObjectLinks**](InterfaceStatisticsResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_statistics_resource_object import InterfaceStatisticsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStatisticsResourceObject from a JSON string
interface_statistics_resource_object_instance = InterfaceStatisticsResourceObject.from_json(json)
# print the JSON string representation of the object
print InterfaceStatisticsResourceObject.to_json()

# convert the object into a dict
interface_statistics_resource_object_dict = interface_statistics_resource_object_instance.to_dict()
# create an instance of InterfaceStatisticsResourceObject from a dict
interface_statistics_resource_object_form_dict = interface_statistics_resource_object.from_dict(interface_statistics_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



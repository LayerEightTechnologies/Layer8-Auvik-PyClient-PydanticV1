# InterfaceStatisticsRelationships

Interface statistics object's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | [**InterfaceStatisticsRelationshipsInterface**](InterfaceStatisticsRelationshipsInterface.md) |  | [optional] 
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_statistics_relationships import InterfaceStatisticsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStatisticsRelationships from a JSON string
interface_statistics_relationships_instance = InterfaceStatisticsRelationships.from_json(json)
# print the JSON string representation of the object
print InterfaceStatisticsRelationships.to_json()

# convert the object into a dict
interface_statistics_relationships_dict = interface_statistics_relationships_instance.to_dict()
# create an instance of InterfaceStatisticsRelationships from a dict
interface_statistics_relationships_form_dict = interface_statistics_relationships.from_dict(interface_statistics_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



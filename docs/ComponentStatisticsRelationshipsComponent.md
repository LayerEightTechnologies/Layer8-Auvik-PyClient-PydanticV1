# ComponentStatisticsRelationshipsComponent

This component the statistics are reported against

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ComponentStatisticsRelationshipsComponentData**](ComponentStatisticsRelationshipsComponentData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_statistics_relationships_component import ComponentStatisticsRelationshipsComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentStatisticsRelationshipsComponent from a JSON string
component_statistics_relationships_component_instance = ComponentStatisticsRelationshipsComponent.from_json(json)
# print the JSON string representation of the object
print ComponentStatisticsRelationshipsComponent.to_json()

# convert the object into a dict
component_statistics_relationships_component_dict = component_statistics_relationships_component_instance.to_dict()
# create an instance of ComponentStatisticsRelationshipsComponent from a dict
component_statistics_relationships_component_form_dict = component_statistics_relationships_component.from_dict(component_statistics_relationships_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



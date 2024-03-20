# ComponentStatisticsRelationships

Component statistics object's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**ComponentStatisticsRelationshipsComponent**](ComponentStatisticsRelationshipsComponent.md) |  | [optional] 
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_statistics_relationships import ComponentStatisticsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentStatisticsRelationships from a JSON string
component_statistics_relationships_instance = ComponentStatisticsRelationships.from_json(json)
# print the JSON string representation of the object
print ComponentStatisticsRelationships.to_json()

# convert the object into a dict
component_statistics_relationships_dict = component_statistics_relationships_instance.to_dict()
# create an instance of ComponentStatisticsRelationships from a dict
component_statistics_relationships_form_dict = component_statistics_relationships.from_dict(component_statistics_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



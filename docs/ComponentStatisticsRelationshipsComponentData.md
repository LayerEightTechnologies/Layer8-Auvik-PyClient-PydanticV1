# ComponentStatisticsRelationshipsComponentData

A component resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This component&#39;s ID | [optional] 
**type** | **str** | The type of the object | [optional] 
**component_name** | **str** | This component&#39;s name | [optional] 
**component_type** | **str** | This component&#39;s type | [optional] 
**parent_device** | **str** | This component&#39;s parent device | [optional] 
**links** | [**ComponentStatisticsRelationshipsComponentDataLinks**](ComponentStatisticsRelationshipsComponentDataLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_statistics_relationships_component_data import ComponentStatisticsRelationshipsComponentData

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentStatisticsRelationshipsComponentData from a JSON string
component_statistics_relationships_component_data_instance = ComponentStatisticsRelationshipsComponentData.from_json(json)
# print the JSON string representation of the object
print ComponentStatisticsRelationshipsComponentData.to_json()

# convert the object into a dict
component_statistics_relationships_component_data_dict = component_statistics_relationships_component_data_instance.to_dict()
# create an instance of ComponentStatisticsRelationshipsComponentData from a dict
component_statistics_relationships_component_data_form_dict = component_statistics_relationships_component_data.from_dict(component_statistics_relationships_component_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



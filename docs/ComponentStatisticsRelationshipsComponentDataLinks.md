# ComponentStatisticsRelationshipsComponentDataLinks

Links relating to this component

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this component&#39;s dashboard in Auvik | [optional] 
**parent_device** | **str** | Link to this component&#39;s parent device dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this set of component info | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_statistics_relationships_component_data_links import ComponentStatisticsRelationshipsComponentDataLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentStatisticsRelationshipsComponentDataLinks from a JSON string
component_statistics_relationships_component_data_links_instance = ComponentStatisticsRelationshipsComponentDataLinks.from_json(json)
# print the JSON string representation of the object
print ComponentStatisticsRelationshipsComponentDataLinks.to_json()

# convert the object into a dict
component_statistics_relationships_component_data_links_dict = component_statistics_relationships_component_data_links_instance.to_dict()
# create an instance of ComponentStatisticsRelationshipsComponentDataLinks from a dict
component_statistics_relationships_component_data_links_form_dict = component_statistics_relationships_component_data_links.from_dict(component_statistics_relationships_component_data_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



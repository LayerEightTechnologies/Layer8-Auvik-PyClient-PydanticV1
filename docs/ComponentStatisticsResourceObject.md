# ComponentStatisticsResourceObject

Component statistics resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID for this statistic | [optional] 
**type** | **str** | The type of this resource object | [optional] 
**attributes** | [**StatisticsAttributes**](StatisticsAttributes.md) |  | [optional] 
**relationships** | [**ComponentStatisticsRelationships**](ComponentStatisticsRelationships.md) |  | [optional] 
**links** | [**ComponentStatisticsResourceObjectLinks**](ComponentStatisticsResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_statistics_resource_object import ComponentStatisticsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentStatisticsResourceObject from a JSON string
component_statistics_resource_object_instance = ComponentStatisticsResourceObject.from_json(json)
# print the JSON string representation of the object
print ComponentStatisticsResourceObject.to_json()

# convert the object into a dict
component_statistics_resource_object_dict = component_statistics_resource_object_instance.to_dict()
# create an instance of ComponentStatisticsResourceObject from a dict
component_statistics_resource_object_form_dict = component_statistics_resource_object.from_dict(component_statistics_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



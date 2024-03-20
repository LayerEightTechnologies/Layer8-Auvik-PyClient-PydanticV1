# ServiceStatisticsResourceObject

Service statistics resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID for this statistic | [optional] 
**type** | **str** | The type of this resource object | [optional] 
**attributes** | [**ServiceStatisticsAttributes**](ServiceStatisticsAttributes.md) |  | [optional] 
**relationships** | [**ServiceStatisticsRelationships**](ServiceStatisticsRelationships.md) |  | [optional] 
**links** | [**ServiceStatisticsResourceObjectLinks**](ServiceStatisticsResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.service_statistics_resource_object import ServiceStatisticsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatisticsResourceObject from a JSON string
service_statistics_resource_object_instance = ServiceStatisticsResourceObject.from_json(json)
# print the JSON string representation of the object
print ServiceStatisticsResourceObject.to_json()

# convert the object into a dict
service_statistics_resource_object_dict = service_statistics_resource_object_instance.to_dict()
# create an instance of ServiceStatisticsResourceObject from a dict
service_statistics_resource_object_form_dict = service_statistics_resource_object.from_dict(service_statistics_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



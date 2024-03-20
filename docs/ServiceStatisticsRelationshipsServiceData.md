# ServiceStatisticsRelationshipsServiceData

A service resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The entity type for a service | [optional] 
**attributes** | [**ServiceStatisticsRelationshipsServiceDataAttributes**](ServiceStatisticsRelationshipsServiceDataAttributes.md) |  | [optional] 
**links** | [**ServiceStatisticsRelationshipsServiceDataLinks**](ServiceStatisticsRelationshipsServiceDataLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.service_statistics_relationships_service_data import ServiceStatisticsRelationshipsServiceData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatisticsRelationshipsServiceData from a JSON string
service_statistics_relationships_service_data_instance = ServiceStatisticsRelationshipsServiceData.from_json(json)
# print the JSON string representation of the object
print ServiceStatisticsRelationshipsServiceData.to_json()

# convert the object into a dict
service_statistics_relationships_service_data_dict = service_statistics_relationships_service_data_instance.to_dict()
# create an instance of ServiceStatisticsRelationshipsServiceData from a dict
service_statistics_relationships_service_data_form_dict = service_statistics_relationships_service_data.from_dict(service_statistics_relationships_service_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



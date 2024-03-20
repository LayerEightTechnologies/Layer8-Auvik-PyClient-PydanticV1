# ServiceStatisticsRelationshipsService

This service the statistics are reported against

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceStatisticsRelationshipsServiceData**](ServiceStatisticsRelationshipsServiceData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.service_statistics_relationships_service import ServiceStatisticsRelationshipsService

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatisticsRelationshipsService from a JSON string
service_statistics_relationships_service_instance = ServiceStatisticsRelationshipsService.from_json(json)
# print the JSON string representation of the object
print ServiceStatisticsRelationshipsService.to_json()

# convert the object into a dict
service_statistics_relationships_service_dict = service_statistics_relationships_service_instance.to_dict()
# create an instance of ServiceStatisticsRelationshipsService from a dict
service_statistics_relationships_service_form_dict = service_statistics_relationships_service.from_dict(service_statistics_relationships_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



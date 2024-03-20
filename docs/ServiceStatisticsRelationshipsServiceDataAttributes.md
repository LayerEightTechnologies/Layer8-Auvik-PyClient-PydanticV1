# ServiceStatisticsRelationshipsServiceDataAttributes

The type-specific properties of the service

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** | A description of the service | [optional] 

## Example

```python
from layer8_auvik_api_client.models.service_statistics_relationships_service_data_attributes import ServiceStatisticsRelationshipsServiceDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatisticsRelationshipsServiceDataAttributes from a JSON string
service_statistics_relationships_service_data_attributes_instance = ServiceStatisticsRelationshipsServiceDataAttributes.from_json(json)
# print the JSON string representation of the object
print ServiceStatisticsRelationshipsServiceDataAttributes.to_json()

# convert the object into a dict
service_statistics_relationships_service_data_attributes_dict = service_statistics_relationships_service_data_attributes_instance.to_dict()
# create an instance of ServiceStatisticsRelationshipsServiceDataAttributes from a dict
service_statistics_relationships_service_data_attributes_form_dict = service_statistics_relationships_service_data_attributes.from_dict(service_statistics_relationships_service_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



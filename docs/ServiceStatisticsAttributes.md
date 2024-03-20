# ServiceStatisticsAttributes

The type-specific properties of the statistics object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_period** | [**ReportPeriod**](ReportPeriod.md) |  | 
**interval** | **str** | The reporting interval for the statistics | 
**stat_type** | **str** | The type of statistic that was returned | [optional] 
**endpoints** | [**List[EndpointStats]**](EndpointStats.md) | Endpoints checked by a cloud ping check service | [optional] 

## Example

```python
from layer8_auvik_api_client.models.service_statistics_attributes import ServiceStatisticsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatisticsAttributes from a JSON string
service_statistics_attributes_instance = ServiceStatisticsAttributes.from_json(json)
# print the JSON string representation of the object
print ServiceStatisticsAttributes.to_json()

# convert the object into a dict
service_statistics_attributes_dict = service_statistics_attributes_instance.to_dict()
# create an instance of ServiceStatisticsAttributes from a dict
service_statistics_attributes_form_dict = service_statistics_attributes.from_dict(service_statistics_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



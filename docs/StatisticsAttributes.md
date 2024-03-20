# StatisticsAttributes

The type-specific properties of the statistics object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_period** | [**ReportPeriod**](ReportPeriod.md) |  | [optional] 
**interval** | **str** | The reporting interval for the statistics | [optional] 
**stat_type** | **str** | The type of statistic that was returned | [optional] 
**stats** | [**List[StatItem]**](StatItem.md) | The list of statistics reported for the entity | [optional] 

## Example

```python
from layer8_auvik_api_client.models.statistics_attributes import StatisticsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsAttributes from a JSON string
statistics_attributes_instance = StatisticsAttributes.from_json(json)
# print the JSON string representation of the object
print StatisticsAttributes.to_json()

# convert the object into a dict
statistics_attributes_dict = statistics_attributes_instance.to_dict()
# create an instance of StatisticsAttributes from a dict
statistics_attributes_form_dict = statistics_attributes.from_dict(statistics_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



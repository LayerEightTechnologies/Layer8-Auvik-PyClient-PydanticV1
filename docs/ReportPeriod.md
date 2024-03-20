# ReportPeriod

Reporting period for the returned statistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_time** | **str** | Start timestamp for the statistics query | [optional] 
**thru_time** | **str** | End timestamp for the statistics query | [optional] 

## Example

```python
from layer8_auvik_api_client.models.report_period import ReportPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPeriod from a JSON string
report_period_instance = ReportPeriod.from_json(json)
# print the JSON string representation of the object
print ReportPeriod.to_json()

# convert the object into a dict
report_period_dict = report_period_instance.to_dict()
# create an instance of ReportPeriod from a dict
report_period_form_dict = report_period.from_dict(report_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



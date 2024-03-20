# SnmpPollerStringHistoryAttributesReportPeriod

Reporting period for the returned historical values

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_time** | **str** | Start timestamp for the query | [optional] 
**thru_time** | **str** | End timestamp for the query | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_string_history_attributes_report_period import SnmpPollerStringHistoryAttributesReportPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerStringHistoryAttributesReportPeriod from a JSON string
snmp_poller_string_history_attributes_report_period_instance = SnmpPollerStringHistoryAttributesReportPeriod.from_json(json)
# print the JSON string representation of the object
print SnmpPollerStringHistoryAttributesReportPeriod.to_json()

# convert the object into a dict
snmp_poller_string_history_attributes_report_period_dict = snmp_poller_string_history_attributes_report_period_instance.to_dict()
# create an instance of SnmpPollerStringHistoryAttributesReportPeriod from a dict
snmp_poller_string_history_attributes_report_period_form_dict = snmp_poller_string_history_attributes_report_period.from_dict(snmp_poller_string_history_attributes_report_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



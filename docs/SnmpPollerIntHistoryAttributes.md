# SnmpPollerIntHistoryAttributes

The type-specific properties of the SNMP Poller Setting's history object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_period** | [**SnmpPollerStringHistoryAttributesReportPeriod**](SnmpPollerStringHistoryAttributesReportPeriod.md) |  | [optional] 
**interval** | **str** | Statistics reporting interval | [optional] 
**stats** | [**List[StatItem2]**](StatItem2.md) | The list of historical values reported for the String SNMP Poller Setting | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_int_history_attributes import SnmpPollerIntHistoryAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerIntHistoryAttributes from a JSON string
snmp_poller_int_history_attributes_instance = SnmpPollerIntHistoryAttributes.from_json(json)
# print the JSON string representation of the object
print SnmpPollerIntHistoryAttributes.to_json()

# convert the object into a dict
snmp_poller_int_history_attributes_dict = snmp_poller_int_history_attributes_instance.to_dict()
# create an instance of SnmpPollerIntHistoryAttributes from a dict
snmp_poller_int_history_attributes_form_dict = snmp_poller_int_history_attributes.from_dict(snmp_poller_int_history_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SnmpPollerStringHistoryRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SnmpPollerStringHistoryResourceObject]**](SnmpPollerStringHistoryResourceObject.md) |  | [optional] 
**links** | [**SnmpPollerStringHistoryReadLinks**](SnmpPollerStringHistoryReadLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_string_history_read import SnmpPollerStringHistoryRead

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerStringHistoryRead from a JSON string
snmp_poller_string_history_read_instance = SnmpPollerStringHistoryRead.from_json(json)
# print the JSON string representation of the object
print SnmpPollerStringHistoryRead.to_json()

# convert the object into a dict
snmp_poller_string_history_read_dict = snmp_poller_string_history_read_instance.to_dict()
# create an instance of SnmpPollerStringHistoryRead from a dict
snmp_poller_string_history_read_form_dict = snmp_poller_string_history_read.from_dict(snmp_poller_string_history_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



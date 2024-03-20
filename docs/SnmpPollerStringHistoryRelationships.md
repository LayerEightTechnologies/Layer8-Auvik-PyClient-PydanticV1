# SnmpPollerStringHistoryRelationships

This history of SNMP Poller Setting's values relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snmp_poller_setting** | [**SnmpPollerSettingReduced**](SnmpPollerSettingReduced.md) |  | [optional] 
**device** | [**Device**](Device.md) |  | [optional] 
**tenant** | [**TenantReduced**](TenantReduced.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_string_history_relationships import SnmpPollerStringHistoryRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerStringHistoryRelationships from a JSON string
snmp_poller_string_history_relationships_instance = SnmpPollerStringHistoryRelationships.from_json(json)
# print the JSON string representation of the object
print SnmpPollerStringHistoryRelationships.to_json()

# convert the object into a dict
snmp_poller_string_history_relationships_dict = snmp_poller_string_history_relationships_instance.to_dict()
# create an instance of SnmpPollerStringHistoryRelationships from a dict
snmp_poller_string_history_relationships_form_dict = snmp_poller_string_history_relationships.from_dict(snmp_poller_string_history_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



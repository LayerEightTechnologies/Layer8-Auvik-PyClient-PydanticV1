# SnmpPollerSettingAttributes2

The type-specific properties of the SNMP Poller Setting object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | SNMP Poller Setting&#39;s name | [optional] 
**protocol** | **str** | Protocol | [optional] 
**oid** | **str** | OID identifier | [optional] 
**type** | **str** | SNMP Poller Setting&#39;s type | [optional] 
**use_as** | **str** | Underlying use of this snmp poller(serialNo, Monitor) | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_attributes2 import SnmpPollerSettingAttributes2

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingAttributes2 from a JSON string
snmp_poller_setting_attributes2_instance = SnmpPollerSettingAttributes2.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingAttributes2.to_json()

# convert the object into a dict
snmp_poller_setting_attributes2_dict = snmp_poller_setting_attributes2_instance.to_dict()
# create an instance of SnmpPollerSettingAttributes2 from a dict
snmp_poller_setting_attributes2_form_dict = snmp_poller_setting_attributes2.from_dict(snmp_poller_setting_attributes2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SnmpPollerSettingReduced

The template for a resource object representing an Auvik SNMP Poller Setting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SnmpPollerSettingReducedData**](SnmpPollerSettingReducedData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_reduced import SnmpPollerSettingReduced

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingReduced from a JSON string
snmp_poller_setting_reduced_instance = SnmpPollerSettingReduced.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingReduced.to_json()

# convert the object into a dict
snmp_poller_setting_reduced_dict = snmp_poller_setting_reduced_instance.to_dict()
# create an instance of SnmpPollerSettingReduced from a dict
snmp_poller_setting_reduced_form_dict = snmp_poller_setting_reduced.from_dict(snmp_poller_setting_reduced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



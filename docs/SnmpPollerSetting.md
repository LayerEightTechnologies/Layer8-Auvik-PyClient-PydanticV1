# SnmpPollerSetting

The template for a resource object representing an Auvik SNMP Poller Setting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SnmpPollerSettingData**](SnmpPollerSettingData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting import SnmpPollerSetting

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSetting from a JSON string
snmp_poller_setting_instance = SnmpPollerSetting.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSetting.to_json()

# convert the object into a dict
snmp_poller_setting_dict = snmp_poller_setting_instance.to_dict()
# create an instance of SnmpPollerSetting from a dict
snmp_poller_setting_form_dict = snmp_poller_setting.from_dict(snmp_poller_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



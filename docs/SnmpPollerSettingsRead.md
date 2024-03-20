# SnmpPollerSettingsRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SnmpPollerSettingsResourceObject]**](SnmpPollerSettingsResourceObject.md) |  | [optional] 
**links** | [**SnmpPollerSettingsReadLinks**](SnmpPollerSettingsReadLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_settings_read import SnmpPollerSettingsRead

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingsRead from a JSON string
snmp_poller_settings_read_instance = SnmpPollerSettingsRead.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingsRead.to_json()

# convert the object into a dict
snmp_poller_settings_read_dict = snmp_poller_settings_read_instance.to_dict()
# create an instance of SnmpPollerSettingsRead from a dict
snmp_poller_settings_read_form_dict = snmp_poller_settings_read.from_dict(snmp_poller_settings_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SnmpPollerSettingDevicesRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SnmpPollerSettingDeviceResourceObject]**](SnmpPollerSettingDeviceResourceObject.md) |  | [optional] 
**links** | [**SnmpPollerSettingDevicesReadLinks**](SnmpPollerSettingDevicesReadLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_devices_read import SnmpPollerSettingDevicesRead

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingDevicesRead from a JSON string
snmp_poller_setting_devices_read_instance = SnmpPollerSettingDevicesRead.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingDevicesRead.to_json()

# convert the object into a dict
snmp_poller_setting_devices_read_dict = snmp_poller_setting_devices_read_instance.to_dict()
# create an instance of SnmpPollerSettingDevicesRead from a dict
snmp_poller_setting_devices_read_form_dict = snmp_poller_setting_devices_read.from_dict(snmp_poller_setting_devices_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



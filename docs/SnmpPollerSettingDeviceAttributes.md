# SnmpPollerSettingDeviceAttributes

The type-specific properties of the Device object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Device name | [optional] 
**type** | **str** | Device type | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_device_attributes import SnmpPollerSettingDeviceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingDeviceAttributes from a JSON string
snmp_poller_setting_device_attributes_instance = SnmpPollerSettingDeviceAttributes.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingDeviceAttributes.to_json()

# convert the object into a dict
snmp_poller_setting_device_attributes_dict = snmp_poller_setting_device_attributes_instance.to_dict()
# create an instance of SnmpPollerSettingDeviceAttributes from a dict
snmp_poller_setting_device_attributes_form_dict = snmp_poller_setting_device_attributes.from_dict(snmp_poller_setting_device_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



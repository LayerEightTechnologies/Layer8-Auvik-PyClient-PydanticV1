# SnmpPollerSettingDeviceRelationships

This device's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**snmp_poller_setting** | [**SnmpPollerSetting**](SnmpPollerSetting.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_device_relationships import SnmpPollerSettingDeviceRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingDeviceRelationships from a JSON string
snmp_poller_setting_device_relationships_instance = SnmpPollerSettingDeviceRelationships.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingDeviceRelationships.to_json()

# convert the object into a dict
snmp_poller_setting_device_relationships_dict = snmp_poller_setting_device_relationships_instance.to_dict()
# create an instance of SnmpPollerSettingDeviceRelationships from a dict
snmp_poller_setting_device_relationships_form_dict = snmp_poller_setting_device_relationships.from_dict(snmp_poller_setting_device_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SnmpPollerSettingData

The type-specific properties of the SNMP Poller's object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API. | [optional] 
**id** | **str** | The unique identifier for a SNMP Poller Setting | [optional] 
**attributes** | [**SnmpPollerSettingDataAttributes**](SnmpPollerSettingDataAttributes.md) |  | [optional] 
**links** | [**DeviceOidMonitorResourceObjectLinks**](DeviceOidMonitorResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_data import SnmpPollerSettingData

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingData from a JSON string
snmp_poller_setting_data_instance = SnmpPollerSettingData.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingData.to_json()

# convert the object into a dict
snmp_poller_setting_data_dict = snmp_poller_setting_data_instance.to_dict()
# create an instance of SnmpPollerSettingData from a dict
snmp_poller_setting_data_form_dict = snmp_poller_setting_data.from_dict(snmp_poller_setting_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



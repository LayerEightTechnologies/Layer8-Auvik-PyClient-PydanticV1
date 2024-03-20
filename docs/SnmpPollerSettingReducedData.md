# SnmpPollerSettingReducedData

The type-specific properties of the SNMP Poller's object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API. | [optional] 
**id** | **str** | The unique identifier for a SNMP Poller Setting | [optional] 
**links** | [**DeviceOidMonitorResourceObjectLinks**](DeviceOidMonitorResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_reduced_data import SnmpPollerSettingReducedData

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingReducedData from a JSON string
snmp_poller_setting_reduced_data_instance = SnmpPollerSettingReducedData.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingReducedData.to_json()

# convert the object into a dict
snmp_poller_setting_reduced_data_dict = snmp_poller_setting_reduced_data_instance.to_dict()
# create an instance of SnmpPollerSettingReducedData from a dict
snmp_poller_setting_reduced_data_form_dict = snmp_poller_setting_reduced_data.from_dict(snmp_poller_setting_reduced_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



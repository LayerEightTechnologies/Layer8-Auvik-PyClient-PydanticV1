# SnmpPollerSettingDataAttributes

The type-specific properties of the tenant object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | SNMP Poller Setting name | [optional] 
**protocol** | **str** | Protocol | [optional] 
**oid** | **str** | OID identifier | [optional] 
**type** | **str** | SNMP Poller Setting type | [optional] 
**use_as** | **str** | Underlying use of this poller (serialNo, poller) | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_data_attributes import SnmpPollerSettingDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingDataAttributes from a JSON string
snmp_poller_setting_data_attributes_instance = SnmpPollerSettingDataAttributes.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingDataAttributes.to_json()

# convert the object into a dict
snmp_poller_setting_data_attributes_dict = snmp_poller_setting_data_attributes_instance.to_dict()
# create an instance of SnmpPollerSettingDataAttributes from a dict
snmp_poller_setting_data_attributes_form_dict = snmp_poller_setting_data_attributes.from_dict(snmp_poller_setting_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



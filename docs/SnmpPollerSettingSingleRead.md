# SnmpPollerSettingSingleRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SnmpPollerSettingSingleResourceObject**](SnmpPollerSettingSingleResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_single_read import SnmpPollerSettingSingleRead

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingSingleRead from a JSON string
snmp_poller_setting_single_read_instance = SnmpPollerSettingSingleRead.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingSingleRead.to_json()

# convert the object into a dict
snmp_poller_setting_single_read_dict = snmp_poller_setting_single_read_instance.to_dict()
# create an instance of SnmpPollerSettingSingleRead from a dict
snmp_poller_setting_single_read_form_dict = snmp_poller_setting_single_read.from_dict(snmp_poller_setting_single_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



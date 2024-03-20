# SnmpPollerSettingRelationships

This SNMP Poller Setting's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_relationships import SnmpPollerSettingRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingRelationships from a JSON string
snmp_poller_setting_relationships_instance = SnmpPollerSettingRelationships.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingRelationships.to_json()

# convert the object into a dict
snmp_poller_setting_relationships_dict = snmp_poller_setting_relationships_instance.to_dict()
# create an instance of SnmpPollerSettingRelationships from a dict
snmp_poller_setting_relationships_form_dict = snmp_poller_setting_relationships.from_dict(snmp_poller_setting_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



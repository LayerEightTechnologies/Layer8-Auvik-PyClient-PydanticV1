# SnmpPollerSettingSingleResourceObject

The template for a resource object representing an Auvik SNMP Poller Setting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for a SNMP Poller Setting | [optional] 
**type** | **str** | The type of object in the API | [optional] 
**attributes** | [**SnmpPollerSettingAttributes**](SnmpPollerSettingAttributes.md) |  | [optional] 
**relationships** | [**SnmpPollerSettingRelationships**](SnmpPollerSettingRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_single_resource_object import SnmpPollerSettingSingleResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingSingleResourceObject from a JSON string
snmp_poller_setting_single_resource_object_instance = SnmpPollerSettingSingleResourceObject.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingSingleResourceObject.to_json()

# convert the object into a dict
snmp_poller_setting_single_resource_object_dict = snmp_poller_setting_single_resource_object_instance.to_dict()
# create an instance of SnmpPollerSettingSingleResourceObject from a dict
snmp_poller_setting_single_resource_object_form_dict = snmp_poller_setting_single_resource_object.from_dict(snmp_poller_setting_single_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



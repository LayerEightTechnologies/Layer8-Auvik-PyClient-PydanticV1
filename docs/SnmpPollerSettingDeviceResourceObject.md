# SnmpPollerSettingDeviceResourceObject

The template for a resource object representing an Auvik Device for a specific SNMP Poller setting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for a device | [optional] 
**type** | **str** | The type of object in the API | [optional] 
**attributes** | [**SnmpPollerSettingDeviceAttributes**](SnmpPollerSettingDeviceAttributes.md) |  | [optional] 
**relationships** | [**SnmpPollerSettingDeviceRelationships**](SnmpPollerSettingDeviceRelationships.md) |  | [optional] 
**links** | [**SnmpPollerSettingDeviceResourceObjectLinks**](SnmpPollerSettingDeviceResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_device_resource_object import SnmpPollerSettingDeviceResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingDeviceResourceObject from a JSON string
snmp_poller_setting_device_resource_object_instance = SnmpPollerSettingDeviceResourceObject.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingDeviceResourceObject.to_json()

# convert the object into a dict
snmp_poller_setting_device_resource_object_dict = snmp_poller_setting_device_resource_object_instance.to_dict()
# create an instance of SnmpPollerSettingDeviceResourceObject from a dict
snmp_poller_setting_device_resource_object_form_dict = snmp_poller_setting_device_resource_object.from_dict(snmp_poller_setting_device_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



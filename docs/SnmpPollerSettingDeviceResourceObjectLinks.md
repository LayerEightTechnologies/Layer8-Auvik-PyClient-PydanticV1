# SnmpPollerSettingDeviceResourceObjectLinks

List of links relating to this OID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this Device&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this OID | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_setting_device_resource_object_links import SnmpPollerSettingDeviceResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingDeviceResourceObjectLinks from a JSON string
snmp_poller_setting_device_resource_object_links_instance = SnmpPollerSettingDeviceResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingDeviceResourceObjectLinks.to_json()

# convert the object into a dict
snmp_poller_setting_device_resource_object_links_dict = snmp_poller_setting_device_resource_object_links_instance.to_dict()
# create an instance of SnmpPollerSettingDeviceResourceObjectLinks from a dict
snmp_poller_setting_device_resource_object_links_form_dict = snmp_poller_setting_device_resource_object_links.from_dict(snmp_poller_setting_device_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



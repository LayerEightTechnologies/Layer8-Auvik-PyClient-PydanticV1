# DeviceOidMonitorResourceObjectLinks

List of links relating to this OID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this OID&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this OID | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_oid_monitor_resource_object_links import DeviceOidMonitorResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOidMonitorResourceObjectLinks from a JSON string
device_oid_monitor_resource_object_links_instance = DeviceOidMonitorResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print DeviceOidMonitorResourceObjectLinks.to_json()

# convert the object into a dict
device_oid_monitor_resource_object_links_dict = device_oid_monitor_resource_object_links_instance.to_dict()
# create an instance of DeviceOidMonitorResourceObjectLinks from a dict
device_oid_monitor_resource_object_links_form_dict = device_oid_monitor_resource_object_links.from_dict(device_oid_monitor_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



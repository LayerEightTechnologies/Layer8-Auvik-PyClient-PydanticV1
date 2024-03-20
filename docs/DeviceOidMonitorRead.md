# DeviceOidMonitorRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeviceOidMonitorResourceObject]**](DeviceOidMonitorResourceObject.md) |  | [optional] 
**links** | [**DeviceOidMonitorReadLinks**](DeviceOidMonitorReadLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_oid_monitor_read import DeviceOidMonitorRead

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOidMonitorRead from a JSON string
device_oid_monitor_read_instance = DeviceOidMonitorRead.from_json(json)
# print the JSON string representation of the object
print DeviceOidMonitorRead.to_json()

# convert the object into a dict
device_oid_monitor_read_dict = device_oid_monitor_read_instance.to_dict()
# create an instance of DeviceOidMonitorRead from a dict
device_oid_monitor_read_form_dict = device_oid_monitor_read.from_dict(device_oid_monitor_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeviceOidMonitorReadLinks

Pagination related links

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page in the data set | [optional] 
**prev** | **str** | Previous page in the data set | [optional] 
**first** | **str** | First page in the data set | [optional] 
**last** | **str** | Last page in the data set | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_oid_monitor_read_links import DeviceOidMonitorReadLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOidMonitorReadLinks from a JSON string
device_oid_monitor_read_links_instance = DeviceOidMonitorReadLinks.from_json(json)
# print the JSON string representation of the object
print DeviceOidMonitorReadLinks.to_json()

# convert the object into a dict
device_oid_monitor_read_links_dict = device_oid_monitor_read_links_instance.to_dict()
# create an instance of DeviceOidMonitorReadLinks from a dict
device_oid_monitor_read_links_form_dict = device_oid_monitor_read_links.from_dict(device_oid_monitor_read_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeviceOidMonitorResourceObject

The template for a resource object representing an Auvik device OID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for an OID | [optional] 
**attributes** | [**OidAttributes**](OidAttributes.md) |  | [optional] 
**relationships** | [**OidRelationships**](OidRelationships.md) |  | [optional] 
**links** | [**DeviceOidMonitorResourceObjectLinks**](DeviceOidMonitorResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_oid_monitor_resource_object import DeviceOidMonitorResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOidMonitorResourceObject from a JSON string
device_oid_monitor_resource_object_instance = DeviceOidMonitorResourceObject.from_json(json)
# print the JSON string representation of the object
print DeviceOidMonitorResourceObject.to_json()

# convert the object into a dict
device_oid_monitor_resource_object_dict = device_oid_monitor_resource_object_instance.to_dict()
# create an instance of DeviceOidMonitorResourceObject from a dict
device_oid_monitor_resource_object_form_dict = device_oid_monitor_resource_object.from_dict(device_oid_monitor_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



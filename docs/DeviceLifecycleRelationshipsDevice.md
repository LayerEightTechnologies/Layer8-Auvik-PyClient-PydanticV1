# DeviceLifecycleRelationshipsDevice

The device corresponding to this configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeviceLifecycleRelationshipsDeviceData**](DeviceLifecycleRelationshipsDeviceData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_lifecycle_relationships_device import DeviceLifecycleRelationshipsDevice

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLifecycleRelationshipsDevice from a JSON string
device_lifecycle_relationships_device_instance = DeviceLifecycleRelationshipsDevice.from_json(json)
# print the JSON string representation of the object
print DeviceLifecycleRelationshipsDevice.to_json()

# convert the object into a dict
device_lifecycle_relationships_device_dict = device_lifecycle_relationships_device_instance.to_dict()
# create an instance of DeviceLifecycleRelationshipsDevice from a dict
device_lifecycle_relationships_device_form_dict = device_lifecycle_relationships_device.from_dict(device_lifecycle_relationships_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



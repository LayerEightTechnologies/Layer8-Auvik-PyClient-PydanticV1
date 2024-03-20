# DeviceLifecycleRelationshipsDeviceData

A device resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for this device | [optional] 
**attributes** | [**DeviceLifecycleRelationshipsDeviceDataAttributes**](DeviceLifecycleRelationshipsDeviceDataAttributes.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_lifecycle_relationships_device_data import DeviceLifecycleRelationshipsDeviceData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLifecycleRelationshipsDeviceData from a JSON string
device_lifecycle_relationships_device_data_instance = DeviceLifecycleRelationshipsDeviceData.from_json(json)
# print the JSON string representation of the object
print DeviceLifecycleRelationshipsDeviceData.to_json()

# convert the object into a dict
device_lifecycle_relationships_device_data_dict = device_lifecycle_relationships_device_data_instance.to_dict()
# create an instance of DeviceLifecycleRelationshipsDeviceData from a dict
device_lifecycle_relationships_device_data_form_dict = device_lifecycle_relationships_device_data.from_dict(device_lifecycle_relationships_device_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



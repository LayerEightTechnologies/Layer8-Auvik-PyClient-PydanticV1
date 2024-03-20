# DeviceLifecycleRelationshipsDeviceDataAttributes

The type-specific properties of the device object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device&#39;s name | 

## Example

```python
from layer8_auvik_api_client.models.device_lifecycle_relationships_device_data_attributes import DeviceLifecycleRelationshipsDeviceDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLifecycleRelationshipsDeviceDataAttributes from a JSON string
device_lifecycle_relationships_device_data_attributes_instance = DeviceLifecycleRelationshipsDeviceDataAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceLifecycleRelationshipsDeviceDataAttributes.to_json()

# convert the object into a dict
device_lifecycle_relationships_device_data_attributes_dict = device_lifecycle_relationships_device_data_attributes_instance.to_dict()
# create an instance of DeviceLifecycleRelationshipsDeviceDataAttributes from a dict
device_lifecycle_relationships_device_data_attributes_form_dict = device_lifecycle_relationships_device_data_attributes.from_dict(device_lifecycle_relationships_device_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



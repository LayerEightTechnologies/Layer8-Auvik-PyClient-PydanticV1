# DeviceStatisticsRelationshipsDevice

This device the statistics are reported against

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeviceStatisticsRelationshipsDeviceData**](DeviceStatisticsRelationshipsDeviceData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_statistics_relationships_device import DeviceStatisticsRelationshipsDevice

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStatisticsRelationshipsDevice from a JSON string
device_statistics_relationships_device_instance = DeviceStatisticsRelationshipsDevice.from_json(json)
# print the JSON string representation of the object
print DeviceStatisticsRelationshipsDevice.to_json()

# convert the object into a dict
device_statistics_relationships_device_dict = device_statistics_relationships_device_instance.to_dict()
# create an instance of DeviceStatisticsRelationshipsDevice from a dict
device_statistics_relationships_device_form_dict = device_statistics_relationships_device.from_dict(device_statistics_relationships_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



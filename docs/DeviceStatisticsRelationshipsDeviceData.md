# DeviceStatisticsRelationshipsDeviceData

A device resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This device&#39;s ID | [optional] 
**type** | **str** | The type of the object | [optional] 
**device_name** | **str** | The name of the device | [optional] 
**device_type** | **str** | The type of the device | [optional] 
**links** | [**InterfaceRelationshipsParentDeviceDataLinks**](InterfaceRelationshipsParentDeviceDataLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_statistics_relationships_device_data import DeviceStatisticsRelationshipsDeviceData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStatisticsRelationshipsDeviceData from a JSON string
device_statistics_relationships_device_data_instance = DeviceStatisticsRelationshipsDeviceData.from_json(json)
# print the JSON string representation of the object
print DeviceStatisticsRelationshipsDeviceData.to_json()

# convert the object into a dict
device_statistics_relationships_device_data_dict = device_statistics_relationships_device_data_instance.to_dict()
# create an instance of DeviceStatisticsRelationshipsDeviceData from a dict
device_statistics_relationships_device_data_form_dict = device_statistics_relationships_device_data.from_dict(device_statistics_relationships_device_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



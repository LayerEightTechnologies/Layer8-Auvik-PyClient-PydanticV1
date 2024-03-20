# DeviceAvailabilityStatisticsRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeviceAvailabilityStatisticsResourceObject**](DeviceAvailabilityStatisticsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_availability_statistics_read import DeviceAvailabilityStatisticsRead

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAvailabilityStatisticsRead from a JSON string
device_availability_statistics_read_instance = DeviceAvailabilityStatisticsRead.from_json(json)
# print the JSON string representation of the object
print DeviceAvailabilityStatisticsRead.to_json()

# convert the object into a dict
device_availability_statistics_read_dict = device_availability_statistics_read_instance.to_dict()
# create an instance of DeviceAvailabilityStatisticsRead from a dict
device_availability_statistics_read_form_dict = device_availability_statistics_read.from_dict(device_availability_statistics_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



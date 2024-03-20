# DeviceStatisticsRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeviceStatisticsResourceObject**](DeviceStatisticsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_statistics_read import DeviceStatisticsRead

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStatisticsRead from a JSON string
device_statistics_read_instance = DeviceStatisticsRead.from_json(json)
# print the JSON string representation of the object
print DeviceStatisticsRead.to_json()

# convert the object into a dict
device_statistics_read_dict = device_statistics_read_instance.to_dict()
# create an instance of DeviceStatisticsRead from a dict
device_statistics_read_form_dict = device_statistics_read.from_dict(device_statistics_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



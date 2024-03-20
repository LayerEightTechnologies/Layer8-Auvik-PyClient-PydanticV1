# DeviceUsageRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeviceUsageResourceObject**](DeviceUsageResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_usage_read import DeviceUsageRead

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageRead from a JSON string
device_usage_read_instance = DeviceUsageRead.from_json(json)
# print the JSON string representation of the object
print DeviceUsageRead.to_json()

# convert the object into a dict
device_usage_read_dict = device_usage_read_instance.to_dict()
# create an instance of DeviceUsageRead from a dict
device_usage_read_form_dict = device_usage_read.from_dict(device_usage_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



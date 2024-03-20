# DeviceInfoReadSingle

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DevicesResourceObject**](DevicesResourceObject.md) |  | [optional] 
**included** | [**List[DeviceDetailsResourceObject]**](DeviceDetailsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_info_read_single import DeviceInfoReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInfoReadSingle from a JSON string
device_info_read_single_instance = DeviceInfoReadSingle.from_json(json)
# print the JSON string representation of the object
print DeviceInfoReadSingle.to_json()

# convert the object into a dict
device_info_read_single_dict = device_info_read_single_instance.to_dict()
# create an instance of DeviceInfoReadSingle from a dict
device_info_read_single_form_dict = device_info_read_single.from_dict(device_info_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



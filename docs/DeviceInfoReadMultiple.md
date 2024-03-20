# DeviceInfoReadMultiple

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DevicesResourceObject]**](DevicesResourceObject.md) |  | [optional] 
**included** | [**List[DeviceDetailsResourceObject]**](DeviceDetailsResourceObject.md) |  | [optional] 
**links** | [**DeviceInfoReadMultipleLinks**](DeviceInfoReadMultipleLinks.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_info_read_multiple import DeviceInfoReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInfoReadMultiple from a JSON string
device_info_read_multiple_instance = DeviceInfoReadMultiple.from_json(json)
# print the JSON string representation of the object
print DeviceInfoReadMultiple.to_json()

# convert the object into a dict
device_info_read_multiple_dict = device_info_read_multiple_instance.to_dict()
# create an instance of DeviceInfoReadMultiple from a dict
device_info_read_multiple_form_dict = device_info_read_multiple.from_dict(device_info_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



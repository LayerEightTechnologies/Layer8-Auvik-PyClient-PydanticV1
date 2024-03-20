# DeviceDetailsExtendedReadSingle

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeviceExtendedDetailResourceObject**](DeviceExtendedDetailResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_extended_read_single import DeviceDetailsExtendedReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsExtendedReadSingle from a JSON string
device_details_extended_read_single_instance = DeviceDetailsExtendedReadSingle.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsExtendedReadSingle.to_json()

# convert the object into a dict
device_details_extended_read_single_dict = device_details_extended_read_single_instance.to_dict()
# create an instance of DeviceDetailsExtendedReadSingle from a dict
device_details_extended_read_single_form_dict = device_details_extended_read_single.from_dict(device_details_extended_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



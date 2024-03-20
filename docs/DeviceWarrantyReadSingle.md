# DeviceWarrantyReadSingle

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeviceWarrantyResourceObject**](DeviceWarrantyResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_warranty_read_single import DeviceWarrantyReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceWarrantyReadSingle from a JSON string
device_warranty_read_single_instance = DeviceWarrantyReadSingle.from_json(json)
# print the JSON string representation of the object
print DeviceWarrantyReadSingle.to_json()

# convert the object into a dict
device_warranty_read_single_dict = device_warranty_read_single_instance.to_dict()
# create an instance of DeviceWarrantyReadSingle from a dict
device_warranty_read_single_form_dict = device_warranty_read_single.from_dict(device_warranty_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



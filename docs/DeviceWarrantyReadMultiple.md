# DeviceWarrantyReadMultiple

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeviceWarrantyResourceObject]**](DeviceWarrantyResourceObject.md) |  | [optional] 
**links** | [**DeviceWarrantyReadMultipleLinks**](DeviceWarrantyReadMultipleLinks.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_warranty_read_multiple import DeviceWarrantyReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceWarrantyReadMultiple from a JSON string
device_warranty_read_multiple_instance = DeviceWarrantyReadMultiple.from_json(json)
# print the JSON string representation of the object
print DeviceWarrantyReadMultiple.to_json()

# convert the object into a dict
device_warranty_read_multiple_dict = device_warranty_read_multiple_instance.to_dict()
# create an instance of DeviceWarrantyReadMultiple from a dict
device_warranty_read_multiple_form_dict = device_warranty_read_multiple.from_dict(device_warranty_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



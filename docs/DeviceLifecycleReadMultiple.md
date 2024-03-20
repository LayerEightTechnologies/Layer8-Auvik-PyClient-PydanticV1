# DeviceLifecycleReadMultiple

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeviceLifecycleResourceObject]**](DeviceLifecycleResourceObject.md) |  | [optional] 
**links** | [**DeviceLifecycleReadMultipleLinks**](DeviceLifecycleReadMultipleLinks.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_lifecycle_read_multiple import DeviceLifecycleReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLifecycleReadMultiple from a JSON string
device_lifecycle_read_multiple_instance = DeviceLifecycleReadMultiple.from_json(json)
# print the JSON string representation of the object
print DeviceLifecycleReadMultiple.to_json()

# convert the object into a dict
device_lifecycle_read_multiple_dict = device_lifecycle_read_multiple_instance.to_dict()
# create an instance of DeviceLifecycleReadMultiple from a dict
device_lifecycle_read_multiple_form_dict = device_lifecycle_read_multiple.from_dict(device_lifecycle_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



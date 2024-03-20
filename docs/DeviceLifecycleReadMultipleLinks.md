# DeviceLifecycleReadMultipleLinks

Pagination related links

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page in the data set | [optional] 
**prev** | **str** | Previous page in the data set | [optional] 
**first** | **str** | First page in the data set | [optional] 
**last** | **str** | Last page in the data set | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_lifecycle_read_multiple_links import DeviceLifecycleReadMultipleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLifecycleReadMultipleLinks from a JSON string
device_lifecycle_read_multiple_links_instance = DeviceLifecycleReadMultipleLinks.from_json(json)
# print the JSON string representation of the object
print DeviceLifecycleReadMultipleLinks.to_json()

# convert the object into a dict
device_lifecycle_read_multiple_links_dict = device_lifecycle_read_multiple_links_instance.to_dict()
# create an instance of DeviceLifecycleReadMultipleLinks from a dict
device_lifecycle_read_multiple_links_form_dict = device_lifecycle_read_multiple_links.from_dict(device_lifecycle_read_multiple_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



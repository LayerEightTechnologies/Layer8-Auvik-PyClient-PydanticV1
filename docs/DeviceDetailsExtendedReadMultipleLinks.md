# DeviceDetailsExtendedReadMultipleLinks

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
from layer8_auvik_api_client.models.device_details_extended_read_multiple_links import DeviceDetailsExtendedReadMultipleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsExtendedReadMultipleLinks from a JSON string
device_details_extended_read_multiple_links_instance = DeviceDetailsExtendedReadMultipleLinks.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsExtendedReadMultipleLinks.to_json()

# convert the object into a dict
device_details_extended_read_multiple_links_dict = device_details_extended_read_multiple_links_instance.to_dict()
# create an instance of DeviceDetailsExtendedReadMultipleLinks from a dict
device_details_extended_read_multiple_links_form_dict = device_details_extended_read_multiple_links.from_dict(device_details_extended_read_multiple_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



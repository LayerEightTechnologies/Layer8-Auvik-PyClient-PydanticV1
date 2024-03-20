# DeviceExtendedDetailsDeviceLinks

List of links relating to this device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Link to this device&#39;s extended details | [optional] 
**info** | **str** | Link to this device&#39;s device info | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_extended_details_device_links import DeviceExtendedDetailsDeviceLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceExtendedDetailsDeviceLinks from a JSON string
device_extended_details_device_links_instance = DeviceExtendedDetailsDeviceLinks.from_json(json)
# print the JSON string representation of the object
print DeviceExtendedDetailsDeviceLinks.to_json()

# convert the object into a dict
device_extended_details_device_links_dict = device_extended_details_device_links_instance.to_dict()
# create an instance of DeviceExtendedDetailsDeviceLinks from a dict
device_extended_details_device_links_form_dict = device_extended_details_device_links.from_dict(device_extended_details_device_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



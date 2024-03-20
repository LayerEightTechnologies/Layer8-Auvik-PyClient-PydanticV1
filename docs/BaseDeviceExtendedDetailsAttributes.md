# BaseDeviceExtendedDetailsAttributes

The type-specific properties of the devices object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device&#39;s name | 
**last_modified** | **str** | When one of this device&#39;s attributes was last modified | [optional] 
**last_seen_time** | **str** | Last seen online date/time of a device | [optional] 

## Example

```python
from layer8_auvik_api_client.models.base_device_extended_details_attributes import BaseDeviceExtendedDetailsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of BaseDeviceExtendedDetailsAttributes from a JSON string
base_device_extended_details_attributes_instance = BaseDeviceExtendedDetailsAttributes.from_json(json)
# print the JSON string representation of the object
print BaseDeviceExtendedDetailsAttributes.to_json()

# convert the object into a dict
base_device_extended_details_attributes_dict = base_device_extended_details_attributes_instance.to_dict()
# create an instance of BaseDeviceExtendedDetailsAttributes from a dict
base_device_extended_details_attributes_form_dict = base_device_extended_details_attributes.from_dict(base_device_extended_details_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



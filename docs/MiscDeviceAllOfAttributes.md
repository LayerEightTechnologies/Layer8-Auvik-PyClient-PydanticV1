# MiscDeviceAllOfAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device&#39;s name | 
**last_modified** | **str** | When one of this device&#39;s attributes was last modified | [optional] 
**last_seen_time** | **str** | Last seen online date/time of a device | [optional] 
**device_type** | **str** | What type of device it is | 
**tunnels** | [**List[MiscDeviceAllOfAttributesAllOfTunnelsInner]**](MiscDeviceAllOfAttributesAllOfTunnelsInner.md) | List of tunnels on the device | 

## Example

```python
from layer8_auvik_api_client.models.misc_device_all_of_attributes import MiscDeviceAllOfAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MiscDeviceAllOfAttributes from a JSON string
misc_device_all_of_attributes_instance = MiscDeviceAllOfAttributes.from_json(json)
# print the JSON string representation of the object
print MiscDeviceAllOfAttributes.to_json()

# convert the object into a dict
misc_device_all_of_attributes_dict = misc_device_all_of_attributes_instance.to_dict()
# create an instance of MiscDeviceAllOfAttributes from a dict
misc_device_all_of_attributes_form_dict = misc_device_all_of_attributes.from_dict(misc_device_all_of_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



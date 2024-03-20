# DeviceAttributes

The type-specific properties of the devices object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addresses** | **List[str]** | Device&#39;s local IP addresses | 
**device_name** | **str** | Device&#39;s name | 
**device_type** | **str** | What type of device it is | 
**make_model** | **str** | Make and model of this device | 
**vendor_name** | **str** | Vendor name for this device | 
**software_version** | **str** | Devices software version, if known | 
**serial_number** | **str** | Device&#39;s serial number | 
**description** | **str** | Description | 
**firmware_version** | **str** | Device&#39;s firmware version | 
**last_modified** | **str** | When one of this device&#39;s attributes was last modified | 
**last_seen_time** | **str** | Last seen online date/time of a device | [optional] 
**online_status** | **str** | Device&#39;s online status | 

## Example

```python
from layer8_auvik_api_client.models.device_attributes import DeviceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAttributes from a JSON string
device_attributes_instance = DeviceAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceAttributes.to_json()

# convert the object into a dict
device_attributes_dict = device_attributes_instance.to_dict()
# create an instance of DeviceAttributes from a dict
device_attributes_form_dict = device_attributes.from_dict(device_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



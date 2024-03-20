# DeviceDetailsAttributes

The type-specific properties of the devices object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_status** | [**DeviceDetailsAttributesDiscoveryStatus**](DeviceDetailsAttributesDiscoveryStatus.md) |  | 
**manage_status** | **bool** | Whether this device is managed by Auvik or not | 
**traffic_insights_status** | **str** | The status of TrafficInsights on this device | 

## Example

```python
from layer8_auvik_api_client.models.device_details_attributes import DeviceDetailsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsAttributes from a JSON string
device_details_attributes_instance = DeviceDetailsAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsAttributes.to_json()

# convert the object into a dict
device_details_attributes_dict = device_details_attributes_instance.to_dict()
# create an instance of DeviceDetailsAttributes from a dict
device_details_attributes_form_dict = device_details_attributes.from_dict(device_details_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



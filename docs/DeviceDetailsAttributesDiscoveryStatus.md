# DeviceDetailsAttributesDiscoveryStatus

High level statuses of discovery services

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snmp** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**wmi** | **str** |  | [optional] 
**vmware** | **str** |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_attributes_discovery_status import DeviceDetailsAttributesDiscoveryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsAttributesDiscoveryStatus from a JSON string
device_details_attributes_discovery_status_instance = DeviceDetailsAttributesDiscoveryStatus.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsAttributesDiscoveryStatus.to_json()

# convert the object into a dict
device_details_attributes_discovery_status_dict = device_details_attributes_discovery_status_instance.to_dict()
# create an instance of DeviceDetailsAttributesDiscoveryStatus from a dict
device_details_attributes_discovery_status_form_dict = device_details_attributes_discovery_status.from_dict(device_details_attributes_discovery_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



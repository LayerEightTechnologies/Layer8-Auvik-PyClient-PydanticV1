# MiscDeviceAllOfAttributesAllOfTunnelsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_phase1** | **str** | The defining name of the first phase within Internet Key Exchange (IKE) tunnel negotiation | 
**name_phase2** | **str** | The defining name of the second phase within Internet Key Exchange (IKE) tunnel negotiation | 
**local_gateway** | **str** | IP address of the local IKE gateway | 
**remote_gateway** | **str** | IP address of the remote IKE gateway | 
**source_begin_ip** | **str** | The first IP address within the range of addresses assigned to IPSec tunnel interfaces on the local device | 
**source_end_ip** | **str** | The last IP address within the range of addresses assigned to IPSec tunnel interfaces on the local device | 
**destination_begin_ip** | **str** | The first IP address within the range of addresses assigned to IPSec tunnel interfaces on the remote device | 
**destination_end_ip** | **str** | The last IP address within the range of addresses assigned to IPSec tunnel interfaces on the remote device | 

## Example

```python
from layer8_auvik_api_client.models.misc_device_all_of_attributes_all_of_tunnels_inner import MiscDeviceAllOfAttributesAllOfTunnelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MiscDeviceAllOfAttributesAllOfTunnelsInner from a JSON string
misc_device_all_of_attributes_all_of_tunnels_inner_instance = MiscDeviceAllOfAttributesAllOfTunnelsInner.from_json(json)
# print the JSON string representation of the object
print MiscDeviceAllOfAttributesAllOfTunnelsInner.to_json()

# convert the object into a dict
misc_device_all_of_attributes_all_of_tunnels_inner_dict = misc_device_all_of_attributes_all_of_tunnels_inner_instance.to_dict()
# create an instance of MiscDeviceAllOfAttributesAllOfTunnelsInner from a dict
misc_device_all_of_attributes_all_of_tunnels_inner_form_dict = misc_device_all_of_attributes_all_of_tunnels_inner.from_dict(misc_device_all_of_attributes_all_of_tunnels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



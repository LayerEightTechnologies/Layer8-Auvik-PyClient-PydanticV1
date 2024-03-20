# HypervisorAllOfAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device&#39;s name | 
**last_modified** | **str** | When one of this device&#39;s attributes was last modified | [optional] 
**last_seen_time** | **str** | Last seen online date/time of a device | [optional] 
**device_type** | **str** | What type of device it is | 
**virtual_machines** | [**List[HypervisorAllOfAttributesAllOfVirtualMachinesInner]**](HypervisorAllOfAttributesAllOfVirtualMachinesInner.md) | List of every VM on this hypervisor | 

## Example

```python
from layer8_auvik_api_client.models.hypervisor_all_of_attributes import HypervisorAllOfAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of HypervisorAllOfAttributes from a JSON string
hypervisor_all_of_attributes_instance = HypervisorAllOfAttributes.from_json(json)
# print the JSON string representation of the object
print HypervisorAllOfAttributes.to_json()

# convert the object into a dict
hypervisor_all_of_attributes_dict = hypervisor_all_of_attributes_instance.to_dict()
# create an instance of HypervisorAllOfAttributes from a dict
hypervisor_all_of_attributes_form_dict = hypervisor_all_of_attributes.from_dict(hypervisor_all_of_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



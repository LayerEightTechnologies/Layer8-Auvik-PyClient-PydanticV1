# HypervisorAllOfAttributesAllOfVirtualMachinesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_type** | **str** | What type of device it is | 
**power_status** | **str** | The VM power status | 
**v_cpu** | **str** | Number of virtual CPUs | 
**v_disk** | **str** | Number of virtual disks | 
**allocated_memory** | **str** | How much memory is allocated to this VM, in Bytes | 
**snapshots** | [**List[HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner]**](HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner.md) | List of image snapshots for this VM | 

## Example

```python
from layer8_auvik_api_client.models.hypervisor_all_of_attributes_all_of_virtual_machines_inner import HypervisorAllOfAttributesAllOfVirtualMachinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of HypervisorAllOfAttributesAllOfVirtualMachinesInner from a JSON string
hypervisor_all_of_attributes_all_of_virtual_machines_inner_instance = HypervisorAllOfAttributesAllOfVirtualMachinesInner.from_json(json)
# print the JSON string representation of the object
print HypervisorAllOfAttributesAllOfVirtualMachinesInner.to_json()

# convert the object into a dict
hypervisor_all_of_attributes_all_of_virtual_machines_inner_dict = hypervisor_all_of_attributes_all_of_virtual_machines_inner_instance.to_dict()
# create an instance of HypervisorAllOfAttributesAllOfVirtualMachinesInner from a dict
hypervisor_all_of_attributes_all_of_virtual_machines_inner_form_dict = hypervisor_all_of_attributes_all_of_virtual_machines_inner.from_dict(hypervisor_all_of_attributes_all_of_virtual_machines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



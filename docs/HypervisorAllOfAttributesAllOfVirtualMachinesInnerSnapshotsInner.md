# HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_name** | **str** | The snapshot&#39;s name | 
**snapshot_description** | **str** | The snapshot&#39;s description | 
**snapshot_date** | **str** | The date the snapshot was taken | 
**snapshot_size** | **str** | File size of the snapshot | 
**parent_snapshot_name** | **str** | Parent snapshot&#39;s name | 

## Example

```python
from layer8_auvik_api_client.models.hypervisor_all_of_attributes_all_of_virtual_machines_inner_snapshots_inner import HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner from a JSON string
hypervisor_all_of_attributes_all_of_virtual_machines_inner_snapshots_inner_instance = HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner.from_json(json)
# print the JSON string representation of the object
print HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner.to_json()

# convert the object into a dict
hypervisor_all_of_attributes_all_of_virtual_machines_inner_snapshots_inner_dict = hypervisor_all_of_attributes_all_of_virtual_machines_inner_snapshots_inner_instance.to_dict()
# create an instance of HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner from a dict
hypervisor_all_of_attributes_all_of_virtual_machines_inner_snapshots_inner_form_dict = hypervisor_all_of_attributes_all_of_virtual_machines_inner_snapshots_inner.from_dict(hypervisor_all_of_attributes_all_of_virtual_machines_inner_snapshots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



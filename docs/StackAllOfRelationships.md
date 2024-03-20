# StackAllOfRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**networks** | [**DeviceRelationshipsNetworks**](DeviceRelationshipsNetworks.md) |  | [optional] 
**device_detail** | [**DeviceRelationshipsDeviceDetail**](DeviceRelationshipsDeviceDetail.md) |  | [optional] 
**members** | [**List[StackAllOfRelationshipsAllOfMembersInner]**](StackAllOfRelationshipsAllOfMembersInner.md) | Members of this stack | [optional] 

## Example

```python
from layer8_auvik_api_client.models.stack_all_of_relationships import StackAllOfRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of StackAllOfRelationships from a JSON string
stack_all_of_relationships_instance = StackAllOfRelationships.from_json(json)
# print the JSON string representation of the object
print StackAllOfRelationships.to_json()

# convert the object into a dict
stack_all_of_relationships_dict = stack_all_of_relationships_instance.to_dict()
# create an instance of StackAllOfRelationships from a dict
stack_all_of_relationships_form_dict = stack_all_of_relationships.from_dict(stack_all_of_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



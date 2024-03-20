# StackAllOfRelationshipsAllOfMembersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Device ID of this stack member | [optional] 
**type** | **str** | Resource type of this stack member | [optional] 
**attributes** | [**StackAllOfRelationshipsAllOfMembersInnerAttributes**](StackAllOfRelationshipsAllOfMembersInnerAttributes.md) |  | [optional] 
**links** | [**StackAllOfRelationshipsAllOfMembersInnerLinks**](StackAllOfRelationshipsAllOfMembersInnerLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.stack_all_of_relationships_all_of_members_inner import StackAllOfRelationshipsAllOfMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of StackAllOfRelationshipsAllOfMembersInner from a JSON string
stack_all_of_relationships_all_of_members_inner_instance = StackAllOfRelationshipsAllOfMembersInner.from_json(json)
# print the JSON string representation of the object
print StackAllOfRelationshipsAllOfMembersInner.to_json()

# convert the object into a dict
stack_all_of_relationships_all_of_members_inner_dict = stack_all_of_relationships_all_of_members_inner_instance.to_dict()
# create an instance of StackAllOfRelationshipsAllOfMembersInner from a dict
stack_all_of_relationships_all_of_members_inner_form_dict = stack_all_of_relationships_all_of_members_inner.from_dict(stack_all_of_relationships_all_of_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



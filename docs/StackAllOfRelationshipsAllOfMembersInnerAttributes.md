# StackAllOfRelationshipsAllOfMembersInnerAttributes

Details about this stack member

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_name** | **str** | The member&#39;s name | 
**make_model** | **str** | The member&#39;s make and model | 
**member_number** | **str** | The member&#39;s number in the stack | 
**member_role** | **str** | The member&#39;s role | 
**member_status** | **str** | The member&#39;s status | 
**mac_address** | **str** | The member&#39;s MAC address | 
**software_priority** | **str** | Software priority of this stack. | 
**hardware_priority** | **str** | Hardware priority of this stack. | 
**serial_number** | **str** | The member&#39;s serial number | 
**software_revision** | **str** | Software revision/version of this stack member | 

## Example

```python
from layer8_auvik_api_client.models.stack_all_of_relationships_all_of_members_inner_attributes import StackAllOfRelationshipsAllOfMembersInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of StackAllOfRelationshipsAllOfMembersInnerAttributes from a JSON string
stack_all_of_relationships_all_of_members_inner_attributes_instance = StackAllOfRelationshipsAllOfMembersInnerAttributes.from_json(json)
# print the JSON string representation of the object
print StackAllOfRelationshipsAllOfMembersInnerAttributes.to_json()

# convert the object into a dict
stack_all_of_relationships_all_of_members_inner_attributes_dict = stack_all_of_relationships_all_of_members_inner_attributes_instance.to_dict()
# create an instance of StackAllOfRelationshipsAllOfMembersInnerAttributes from a dict
stack_all_of_relationships_all_of_members_inner_attributes_form_dict = stack_all_of_relationships_all_of_members_inner_attributes.from_dict(stack_all_of_relationships_all_of_members_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



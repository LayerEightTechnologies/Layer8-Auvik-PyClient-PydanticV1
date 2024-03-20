# InterfaceRelationships

This interface's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**connected_to** | [**InterfaceRelationshipsConnectedTo**](InterfaceRelationshipsConnectedTo.md) |  | [optional] 
**networks** | [**InterfaceRelationshipsNetworks**](InterfaceRelationshipsNetworks.md) |  | [optional] 
**parent_device** | [**InterfaceRelationshipsParentDevice**](InterfaceRelationshipsParentDevice.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_relationships import InterfaceRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRelationships from a JSON string
interface_relationships_instance = InterfaceRelationships.from_json(json)
# print the JSON string representation of the object
print InterfaceRelationships.to_json()

# convert the object into a dict
interface_relationships_dict = interface_relationships_instance.to_dict()
# create an instance of InterfaceRelationships from a dict
interface_relationships_form_dict = interface_relationships.from_dict(interface_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InterfaceRelationshipsNetworks

This interface's networks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InterfaceRelationshipsNetworksData]**](InterfaceRelationshipsNetworksData.md) | An network resource object | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_relationships_networks import InterfaceRelationshipsNetworks

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRelationshipsNetworks from a JSON string
interface_relationships_networks_instance = InterfaceRelationshipsNetworks.from_json(json)
# print the JSON string representation of the object
print InterfaceRelationshipsNetworks.to_json()

# convert the object into a dict
interface_relationships_networks_dict = interface_relationships_networks_instance.to_dict()
# create an instance of InterfaceRelationshipsNetworks from a dict
interface_relationships_networks_form_dict = interface_relationships_networks.from_dict(interface_relationships_networks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



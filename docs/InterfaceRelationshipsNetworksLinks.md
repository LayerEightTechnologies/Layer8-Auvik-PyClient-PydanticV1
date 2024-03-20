# InterfaceRelationshipsNetworksLinks

Links relating to this network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this network&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this set of network info | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_relationships_networks_links import InterfaceRelationshipsNetworksLinks

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRelationshipsNetworksLinks from a JSON string
interface_relationships_networks_links_instance = InterfaceRelationshipsNetworksLinks.from_json(json)
# print the JSON string representation of the object
print InterfaceRelationshipsNetworksLinks.to_json()

# convert the object into a dict
interface_relationships_networks_links_dict = interface_relationships_networks_links_instance.to_dict()
# create an instance of InterfaceRelationshipsNetworksLinks from a dict
interface_relationships_networks_links_form_dict = interface_relationships_networks_links.from_dict(interface_relationships_networks_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



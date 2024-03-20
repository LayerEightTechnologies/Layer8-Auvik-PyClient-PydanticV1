# InterfaceRelationshipsConnectedToLinks

Links relating to this interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this interface&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this set of network info | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_relationships_connected_to_links import InterfaceRelationshipsConnectedToLinks

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRelationshipsConnectedToLinks from a JSON string
interface_relationships_connected_to_links_instance = InterfaceRelationshipsConnectedToLinks.from_json(json)
# print the JSON string representation of the object
print InterfaceRelationshipsConnectedToLinks.to_json()

# convert the object into a dict
interface_relationships_connected_to_links_dict = interface_relationships_connected_to_links_instance.to_dict()
# create an instance of InterfaceRelationshipsConnectedToLinks from a dict
interface_relationships_connected_to_links_form_dict = interface_relationships_connected_to_links.from_dict(interface_relationships_connected_to_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



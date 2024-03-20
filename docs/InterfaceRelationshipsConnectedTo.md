# InterfaceRelationshipsConnectedTo

List of other interfaces this interface is connected to

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InterfaceRelationshipsConnectedToData]**](InterfaceRelationshipsConnectedToData.md) | An interface resource object | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_relationships_connected_to import InterfaceRelationshipsConnectedTo

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRelationshipsConnectedTo from a JSON string
interface_relationships_connected_to_instance = InterfaceRelationshipsConnectedTo.from_json(json)
# print the JSON string representation of the object
print InterfaceRelationshipsConnectedTo.to_json()

# convert the object into a dict
interface_relationships_connected_to_dict = interface_relationships_connected_to_instance.to_dict()
# create an instance of InterfaceRelationshipsConnectedTo from a dict
interface_relationships_connected_to_form_dict = interface_relationships_connected_to.from_dict(interface_relationships_connected_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



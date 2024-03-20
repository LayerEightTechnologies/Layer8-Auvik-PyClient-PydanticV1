# InterfaceRelationshipsConnectedToData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This interface&#39;s ID | [optional] 
**type** | **str** | The type of the object | [optional] 
**links** | [**InterfaceRelationshipsConnectedToLinks**](InterfaceRelationshipsConnectedToLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_relationships_connected_to_data import InterfaceRelationshipsConnectedToData

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRelationshipsConnectedToData from a JSON string
interface_relationships_connected_to_data_instance = InterfaceRelationshipsConnectedToData.from_json(json)
# print the JSON string representation of the object
print InterfaceRelationshipsConnectedToData.to_json()

# convert the object into a dict
interface_relationships_connected_to_data_dict = interface_relationships_connected_to_data_instance.to_dict()
# create an instance of InterfaceRelationshipsConnectedToData from a dict
interface_relationships_connected_to_data_form_dict = interface_relationships_connected_to_data.from_dict(interface_relationships_connected_to_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



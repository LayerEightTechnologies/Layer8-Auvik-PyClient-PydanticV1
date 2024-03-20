# InterfaceRelationshipsNetworksData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the object | [optional] 
**id** | **str** | The unique identifier for this network | [optional] 
**attributes** | [**DeviceRelationshipsNetworksAttributes**](DeviceRelationshipsNetworksAttributes.md) |  | [optional] 
**links** | [**InterfaceRelationshipsNetworksLinks**](InterfaceRelationshipsNetworksLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_relationships_networks_data import InterfaceRelationshipsNetworksData

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRelationshipsNetworksData from a JSON string
interface_relationships_networks_data_instance = InterfaceRelationshipsNetworksData.from_json(json)
# print the JSON string representation of the object
print InterfaceRelationshipsNetworksData.to_json()

# convert the object into a dict
interface_relationships_networks_data_dict = interface_relationships_networks_data_instance.to_dict()
# create an instance of InterfaceRelationshipsNetworksData from a dict
interface_relationships_networks_data_form_dict = interface_relationships_networks_data.from_dict(interface_relationships_networks_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



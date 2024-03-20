# DeviceRelationshipsNetworksLinks

Links relating to this network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Link to this network | [optional] 
**dashboard** | **str** | Link to this network&#39;s dashboard in Auvik | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_relationships_networks_links import DeviceRelationshipsNetworksLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRelationshipsNetworksLinks from a JSON string
device_relationships_networks_links_instance = DeviceRelationshipsNetworksLinks.from_json(json)
# print the JSON string representation of the object
print DeviceRelationshipsNetworksLinks.to_json()

# convert the object into a dict
device_relationships_networks_links_dict = device_relationships_networks_links_instance.to_dict()
# create an instance of DeviceRelationshipsNetworksLinks from a dict
device_relationships_networks_links_form_dict = device_relationships_networks_links.from_dict(device_relationships_networks_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



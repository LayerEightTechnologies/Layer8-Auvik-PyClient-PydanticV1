# NetworkRelationshipsDevicesLinks

Links relating to this device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this device&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this device | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_relationships_devices_links import NetworkRelationshipsDevicesLinks

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRelationshipsDevicesLinks from a JSON string
network_relationships_devices_links_instance = NetworkRelationshipsDevicesLinks.from_json(json)
# print the JSON string representation of the object
print NetworkRelationshipsDevicesLinks.to_json()

# convert the object into a dict
network_relationships_devices_links_dict = network_relationships_devices_links_instance.to_dict()
# create an instance of NetworkRelationshipsDevicesLinks from a dict
network_relationships_devices_links_form_dict = network_relationships_devices_links.from_dict(network_relationships_devices_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



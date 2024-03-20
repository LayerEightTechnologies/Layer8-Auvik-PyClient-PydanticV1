# DeviceRelationshipsNetworksAttributes

The type-specific properties of the interfaces object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_name** | **str** | Identifier of the network, usually an IP/subnet or an SSID | 

## Example

```python
from layer8_auvik_api_client.models.device_relationships_networks_attributes import DeviceRelationshipsNetworksAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRelationshipsNetworksAttributes from a JSON string
device_relationships_networks_attributes_instance = DeviceRelationshipsNetworksAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceRelationshipsNetworksAttributes.to_json()

# convert the object into a dict
device_relationships_networks_attributes_dict = device_relationships_networks_attributes_instance.to_dict()
# create an instance of DeviceRelationshipsNetworksAttributes from a dict
device_relationships_networks_attributes_form_dict = device_relationships_networks_attributes.from_dict(device_relationships_networks_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



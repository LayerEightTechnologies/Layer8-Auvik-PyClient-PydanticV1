# DeviceRelationshipsNetworks

This device's networks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeviceRelationshipsNetworksData]**](DeviceRelationshipsNetworksData.md) | An network resource object | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_relationships_networks import DeviceRelationshipsNetworks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRelationshipsNetworks from a JSON string
device_relationships_networks_instance = DeviceRelationshipsNetworks.from_json(json)
# print the JSON string representation of the object
print DeviceRelationshipsNetworks.to_json()

# convert the object into a dict
device_relationships_networks_dict = device_relationships_networks_instance.to_dict()
# create an instance of DeviceRelationshipsNetworks from a dict
device_relationships_networks_form_dict = device_relationships_networks.from_dict(device_relationships_networks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



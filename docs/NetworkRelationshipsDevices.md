# NetworkRelationshipsDevices

This network's devices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NetworkRelationshipsDevicesData]**](NetworkRelationshipsDevicesData.md) | A device resource object | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_relationships_devices import NetworkRelationshipsDevices

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRelationshipsDevices from a JSON string
network_relationships_devices_instance = NetworkRelationshipsDevices.from_json(json)
# print the JSON string representation of the object
print NetworkRelationshipsDevices.to_json()

# convert the object into a dict
network_relationships_devices_dict = network_relationships_devices_instance.to_dict()
# create an instance of NetworkRelationshipsDevices from a dict
network_relationships_devices_form_dict = network_relationships_devices.from_dict(network_relationships_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



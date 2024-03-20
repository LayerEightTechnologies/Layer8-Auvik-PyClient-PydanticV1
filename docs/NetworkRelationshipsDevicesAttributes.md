# NetworkRelationshipsDevicesAttributes

This device's attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device&#39;s name | 

## Example

```python
from layer8_auvik_api_client.models.network_relationships_devices_attributes import NetworkRelationshipsDevicesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRelationshipsDevicesAttributes from a JSON string
network_relationships_devices_attributes_instance = NetworkRelationshipsDevicesAttributes.from_json(json)
# print the JSON string representation of the object
print NetworkRelationshipsDevicesAttributes.to_json()

# convert the object into a dict
network_relationships_devices_attributes_dict = network_relationships_devices_attributes_instance.to_dict()
# create an instance of NetworkRelationshipsDevicesAttributes from a dict
network_relationships_devices_attributes_form_dict = network_relationships_devices_attributes.from_dict(network_relationships_devices_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



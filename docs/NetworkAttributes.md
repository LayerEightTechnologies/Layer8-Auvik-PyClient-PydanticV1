# NetworkAttributes

The type-specific properties of the networks object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_type** | **str** | This network&#39;s type | 
**network_name** | **str** | Name of this network, usually an IP/subnet or an SSID | 
**description** | **str** | Description of this network, also often an IP/subnet or an SSID | 
**scan_status** | **str** | If this network is set to be scanned or not | 
**last_modified** | **str** | When one of this network&#39;s attributes was last modified | 

## Example

```python
from layer8_auvik_api_client.models.network_attributes import NetworkAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAttributes from a JSON string
network_attributes_instance = NetworkAttributes.from_json(json)
# print the JSON string representation of the object
print NetworkAttributes.to_json()

# convert the object into a dict
network_attributes_dict = network_attributes_instance.to_dict()
# create an instance of NetworkAttributes from a dict
network_attributes_form_dict = network_attributes.from_dict(network_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



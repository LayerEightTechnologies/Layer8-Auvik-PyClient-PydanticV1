# NetworkDetailsAttributes

The type-specific properties of the networks object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | Whether this network is a private or public network | 
**primary_collector** | **str** | UUID of the primary Auvik collector assigned to this network | 
**secondary_collectors** | **List[str]** | List of UUIDs of secondary Auvik collectors assigned to this network, if any | 
**collector_selection** | **str** | How collectors for this network are selected | 
**excluded_ip_addresses** | **List[str]** | IP addresses and IP address ranges on this network that have been excluded from scans | 

## Example

```python
from layer8_auvik_api_client.models.network_details_attributes import NetworkDetailsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDetailsAttributes from a JSON string
network_details_attributes_instance = NetworkDetailsAttributes.from_json(json)
# print the JSON string representation of the object
print NetworkDetailsAttributes.to_json()

# convert the object into a dict
network_details_attributes_dict = network_details_attributes_instance.to_dict()
# create an instance of NetworkDetailsAttributes from a dict
network_details_attributes_form_dict = network_details_attributes.from_dict(network_details_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



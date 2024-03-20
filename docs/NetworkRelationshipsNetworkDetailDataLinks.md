# NetworkRelationshipsNetworkDetailDataLinks

Links relating to this network details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Link to this set of network detail | [optional] 
**dashboard** | **str** | Link to this network&#39;s dashboard in Auvik | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_relationships_network_detail_data_links import NetworkRelationshipsNetworkDetailDataLinks

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRelationshipsNetworkDetailDataLinks from a JSON string
network_relationships_network_detail_data_links_instance = NetworkRelationshipsNetworkDetailDataLinks.from_json(json)
# print the JSON string representation of the object
print NetworkRelationshipsNetworkDetailDataLinks.to_json()

# convert the object into a dict
network_relationships_network_detail_data_links_dict = network_relationships_network_detail_data_links_instance.to_dict()
# create an instance of NetworkRelationshipsNetworkDetailDataLinks from a dict
network_relationships_network_detail_data_links_form_dict = network_relationships_network_detail_data_links.from_dict(network_relationships_network_detail_data_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



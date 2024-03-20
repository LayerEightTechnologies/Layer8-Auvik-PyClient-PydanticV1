# NetworkRelationshipsNetworkDetail

Additional attributes and details relating to this network.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NetworkRelationshipsNetworkDetailData**](NetworkRelationshipsNetworkDetailData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_relationships_network_detail import NetworkRelationshipsNetworkDetail

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRelationshipsNetworkDetail from a JSON string
network_relationships_network_detail_instance = NetworkRelationshipsNetworkDetail.from_json(json)
# print the JSON string representation of the object
print NetworkRelationshipsNetworkDetail.to_json()

# convert the object into a dict
network_relationships_network_detail_dict = network_relationships_network_detail_instance.to_dict()
# create an instance of NetworkRelationshipsNetworkDetail from a dict
network_relationships_network_detail_form_dict = network_relationships_network_detail.from_dict(network_relationships_network_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



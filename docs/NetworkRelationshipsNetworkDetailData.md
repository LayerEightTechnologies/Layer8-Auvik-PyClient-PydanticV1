# NetworkRelationshipsNetworkDetailData

A network detail object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for this network | [optional] 
**links** | [**NetworkRelationshipsNetworkDetailDataLinks**](NetworkRelationshipsNetworkDetailDataLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_relationships_network_detail_data import NetworkRelationshipsNetworkDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRelationshipsNetworkDetailData from a JSON string
network_relationships_network_detail_data_instance = NetworkRelationshipsNetworkDetailData.from_json(json)
# print the JSON string representation of the object
print NetworkRelationshipsNetworkDetailData.to_json()

# convert the object into a dict
network_relationships_network_detail_data_dict = network_relationships_network_detail_data_instance.to_dict()
# create an instance of NetworkRelationshipsNetworkDetailData from a dict
network_relationships_network_detail_data_form_dict = network_relationships_network_detail_data.from_dict(network_relationships_network_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



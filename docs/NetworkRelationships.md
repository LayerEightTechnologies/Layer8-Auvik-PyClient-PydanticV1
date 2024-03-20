# NetworkRelationships

This network's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_detail** | [**NetworkRelationshipsNetworkDetail**](NetworkRelationshipsNetworkDetail.md) |  | [optional] 
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**devices** | [**NetworkRelationshipsDevices**](NetworkRelationshipsDevices.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_relationships import NetworkRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRelationships from a JSON string
network_relationships_instance = NetworkRelationships.from_json(json)
# print the JSON string representation of the object
print NetworkRelationships.to_json()

# convert the object into a dict
network_relationships_dict = network_relationships_instance.to_dict()
# create an instance of NetworkRelationships from a dict
network_relationships_form_dict = network_relationships.from_dict(network_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



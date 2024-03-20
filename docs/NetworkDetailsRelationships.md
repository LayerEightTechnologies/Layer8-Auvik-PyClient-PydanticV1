# NetworkDetailsRelationships

This network's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_details_relationships import NetworkDetailsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDetailsRelationships from a JSON string
network_details_relationships_instance = NetworkDetailsRelationships.from_json(json)
# print the JSON string representation of the object
print NetworkDetailsRelationships.to_json()

# convert the object into a dict
network_details_relationships_dict = network_details_relationships_instance.to_dict()
# create an instance of NetworkDetailsRelationships from a dict
network_details_relationships_form_dict = network_details_relationships.from_dict(network_details_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



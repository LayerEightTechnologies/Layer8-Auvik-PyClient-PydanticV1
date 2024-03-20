# ClientUsageRelationships

Client usage object's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**ClientUsageRelationshipsDevices**](ClientUsageRelationshipsDevices.md) |  | [optional] 
**clients** | [**ClientUsageRelationshipsClients**](ClientUsageRelationshipsClients.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_relationships import ClientUsageRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageRelationships from a JSON string
client_usage_relationships_instance = ClientUsageRelationships.from_json(json)
# print the JSON string representation of the object
print ClientUsageRelationships.to_json()

# convert the object into a dict
client_usage_relationships_dict = client_usage_relationships_instance.to_dict()
# create an instance of ClientUsageRelationships from a dict
client_usage_relationships_form_dict = client_usage_relationships.from_dict(client_usage_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



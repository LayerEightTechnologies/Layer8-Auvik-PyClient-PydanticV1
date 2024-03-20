# ClientUsageRelationshipsClients

List of clients' usage (if any) under this client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientUsageRelationshipsClientsData]**](ClientUsageRelationshipsClientsData.md) | A client&#39;s usage for the given usage period | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_relationships_clients import ClientUsageRelationshipsClients

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageRelationshipsClients from a JSON string
client_usage_relationships_clients_instance = ClientUsageRelationshipsClients.from_json(json)
# print the JSON string representation of the object
print ClientUsageRelationshipsClients.to_json()

# convert the object into a dict
client_usage_relationships_clients_dict = client_usage_relationships_clients_instance.to_dict()
# create an instance of ClientUsageRelationshipsClients from a dict
client_usage_relationships_clients_form_dict = client_usage_relationships_clients.from_dict(client_usage_relationships_clients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ClientUsageRelationshipsClientsAttributes

The type-specific properties of the device usage object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_prefix** | **str** | Client tenant&#39;s domain prefix/name | [optional] 
**total_billable_days** | **float** | Total billable days for this client across the usage period | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_relationships_clients_attributes import ClientUsageRelationshipsClientsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageRelationshipsClientsAttributes from a JSON string
client_usage_relationships_clients_attributes_instance = ClientUsageRelationshipsClientsAttributes.from_json(json)
# print the JSON string representation of the object
print ClientUsageRelationshipsClientsAttributes.to_json()

# convert the object into a dict
client_usage_relationships_clients_attributes_dict = client_usage_relationships_clients_attributes_instance.to_dict()
# create an instance of ClientUsageRelationshipsClientsAttributes from a dict
client_usage_relationships_clients_attributes_form_dict = client_usage_relationships_clients_attributes.from_dict(client_usage_relationships_clients_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



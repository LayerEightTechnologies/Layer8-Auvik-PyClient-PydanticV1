# ClientUsageRelationshipsClientsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Client&#39;s ID | [optional] 
**type** | **str** | The type of this resource object | [optional] 
**attributes** | [**ClientUsageRelationshipsClientsAttributes**](ClientUsageRelationshipsClientsAttributes.md) |  | [optional] 
**links** | [**ClientUsageRelationshipsClientsLinks**](ClientUsageRelationshipsClientsLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_relationships_clients_data import ClientUsageRelationshipsClientsData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageRelationshipsClientsData from a JSON string
client_usage_relationships_clients_data_instance = ClientUsageRelationshipsClientsData.from_json(json)
# print the JSON string representation of the object
print ClientUsageRelationshipsClientsData.to_json()

# convert the object into a dict
client_usage_relationships_clients_data_dict = client_usage_relationships_clients_data_instance.to_dict()
# create an instance of ClientUsageRelationshipsClientsData from a dict
client_usage_relationships_clients_data_form_dict = client_usage_relationships_clients_data.from_dict(client_usage_relationships_clients_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



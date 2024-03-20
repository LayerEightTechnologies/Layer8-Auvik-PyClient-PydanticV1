# ClientUsageRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientUsageResourceObject]**](ClientUsageResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_read import ClientUsageRead

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageRead from a JSON string
client_usage_read_instance = ClientUsageRead.from_json(json)
# print the JSON string representation of the object
print ClientUsageRead.to_json()

# convert the object into a dict
client_usage_read_dict = client_usage_read_instance.to_dict()
# create an instance of ClientUsageRead from a dict
client_usage_read_form_dict = client_usage_read.from_dict(client_usage_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



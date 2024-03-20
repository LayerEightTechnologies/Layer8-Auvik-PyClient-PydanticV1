# DeviceUsageRelationshipsClient

Client who owns this device and whose usage this device contributes to.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeviceUsageRelationshipsClientData**](DeviceUsageRelationshipsClientData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_usage_relationships_client import DeviceUsageRelationshipsClient

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageRelationshipsClient from a JSON string
device_usage_relationships_client_instance = DeviceUsageRelationshipsClient.from_json(json)
# print the JSON string representation of the object
print DeviceUsageRelationshipsClient.to_json()

# convert the object into a dict
device_usage_relationships_client_dict = device_usage_relationships_client_instance.to_dict()
# create an instance of DeviceUsageRelationshipsClient from a dict
device_usage_relationships_client_form_dict = device_usage_relationships_client.from_dict(device_usage_relationships_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ClientUsageRelationshipsDevices

List of billable device usage under this client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientUsageRelationshipsDevicesData]**](ClientUsageRelationshipsDevicesData.md) | A device&#39;s usage for the given usage period | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_relationships_devices import ClientUsageRelationshipsDevices

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageRelationshipsDevices from a JSON string
client_usage_relationships_devices_instance = ClientUsageRelationshipsDevices.from_json(json)
# print the JSON string representation of the object
print ClientUsageRelationshipsDevices.to_json()

# convert the object into a dict
client_usage_relationships_devices_dict = client_usage_relationships_devices_instance.to_dict()
# create an instance of ClientUsageRelationshipsDevices from a dict
client_usage_relationships_devices_form_dict = client_usage_relationships_devices.from_dict(client_usage_relationships_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



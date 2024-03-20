# ClientUsageRelationshipsDevicesLinks

Links relating to this device's usage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_record** | **str** | Link to this device&#39;s record in the Device Info API | [optional] 
**var_self** | **str** | Link to this device&#39;s usage in the Usage API | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_relationships_devices_links import ClientUsageRelationshipsDevicesLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageRelationshipsDevicesLinks from a JSON string
client_usage_relationships_devices_links_instance = ClientUsageRelationshipsDevicesLinks.from_json(json)
# print the JSON string representation of the object
print ClientUsageRelationshipsDevicesLinks.to_json()

# convert the object into a dict
client_usage_relationships_devices_links_dict = client_usage_relationships_devices_links_instance.to_dict()
# create an instance of ClientUsageRelationshipsDevicesLinks from a dict
client_usage_relationships_devices_links_form_dict = client_usage_relationships_devices_links.from_dict(client_usage_relationships_devices_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



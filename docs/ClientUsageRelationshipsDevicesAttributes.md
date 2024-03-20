# ClientUsageRelationshipsDevicesAttributes

The type-specific properties of the device usage object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Device&#39;s name | [optional] 
**total_days** | **float** | Total billable days for this device across the usage period | [optional] 
**client_name** | **str** | This device&#39;s owning client&#39;s name/domainPrefix | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_relationships_devices_attributes import ClientUsageRelationshipsDevicesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageRelationshipsDevicesAttributes from a JSON string
client_usage_relationships_devices_attributes_instance = ClientUsageRelationshipsDevicesAttributes.from_json(json)
# print the JSON string representation of the object
print ClientUsageRelationshipsDevicesAttributes.to_json()

# convert the object into a dict
client_usage_relationships_devices_attributes_dict = client_usage_relationships_devices_attributes_instance.to_dict()
# create an instance of ClientUsageRelationshipsDevicesAttributes from a dict
client_usage_relationships_devices_attributes_form_dict = client_usage_relationships_devices_attributes.from_dict(client_usage_relationships_devices_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



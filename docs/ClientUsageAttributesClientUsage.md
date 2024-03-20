# ClientUsageAttributesClientUsage

Roll up of client usage for this client (and its children if a multi-client)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_days** | **float** | Total billable client days for this client (and its children) across the usage period | [optional] 
**averaged_days** | **float** | Average billable client days for this client (and its children) across the usage period | [optional] 
**total_days_by_client_type** | [**ClientUsageAttributesClientUsageTotalDaysByClientType**](ClientUsageAttributesClientUsageTotalDaysByClientType.md) |  | [optional] 
**average_days_by_client_type** | [**ClientUsageAttributesClientUsageAverageDaysByClientType**](ClientUsageAttributesClientUsageAverageDaysByClientType.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_attributes_client_usage import ClientUsageAttributesClientUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageAttributesClientUsage from a JSON string
client_usage_attributes_client_usage_instance = ClientUsageAttributesClientUsage.from_json(json)
# print the JSON string representation of the object
print ClientUsageAttributesClientUsage.to_json()

# convert the object into a dict
client_usage_attributes_client_usage_dict = client_usage_attributes_client_usage_instance.to_dict()
# create an instance of ClientUsageAttributesClientUsage from a dict
client_usage_attributes_client_usage_form_dict = client_usage_attributes_client_usage.from_dict(client_usage_attributes_client_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



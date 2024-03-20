# ClientUsageAttributesClientUsageTotalDaysByClientType

The total billable client days for this client and all of its children across the usage period, by client type, starting on April 1st, 2021

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notier** | **float** | Billable client days for clients with no set client type | [optional] 
**light** | **float** | Billable client days for clients set to Light | [optional] 
**essentials** | **float** | Billable client days for clients set to Essentials | [optional] 
**performance** | **float** | Billable client days for clients set to Performance | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_attributes_client_usage_total_days_by_client_type import ClientUsageAttributesClientUsageTotalDaysByClientType

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageAttributesClientUsageTotalDaysByClientType from a JSON string
client_usage_attributes_client_usage_total_days_by_client_type_instance = ClientUsageAttributesClientUsageTotalDaysByClientType.from_json(json)
# print the JSON string representation of the object
print ClientUsageAttributesClientUsageTotalDaysByClientType.to_json()

# convert the object into a dict
client_usage_attributes_client_usage_total_days_by_client_type_dict = client_usage_attributes_client_usage_total_days_by_client_type_instance.to_dict()
# create an instance of ClientUsageAttributesClientUsageTotalDaysByClientType from a dict
client_usage_attributes_client_usage_total_days_by_client_type_form_dict = client_usage_attributes_client_usage_total_days_by_client_type.from_dict(client_usage_attributes_client_usage_total_days_by_client_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



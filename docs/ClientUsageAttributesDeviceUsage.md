# ClientUsageAttributesDeviceUsage

Roll up of device usage on this client (and its children if a multi-client)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_days** | **float** | The total billable device days for this client and all of its children across the usage period | [optional] 
**average_days** | **float** | The average billable device days for this client and all of its children across the usage period | [optional] 
**total_days_by_client_type** | [**ClientUsageAttributesDeviceUsageTotalDaysByClientType**](ClientUsageAttributesDeviceUsageTotalDaysByClientType.md) |  | [optional] 
**average_days_by_client_type** | [**ClientUsageAttributesDeviceUsageAverageDaysByClientType**](ClientUsageAttributesDeviceUsageAverageDaysByClientType.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_attributes_device_usage import ClientUsageAttributesDeviceUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageAttributesDeviceUsage from a JSON string
client_usage_attributes_device_usage_instance = ClientUsageAttributesDeviceUsage.from_json(json)
# print the JSON string representation of the object
print ClientUsageAttributesDeviceUsage.to_json()

# convert the object into a dict
client_usage_attributes_device_usage_dict = client_usage_attributes_device_usage_instance.to_dict()
# create an instance of ClientUsageAttributesDeviceUsage from a dict
client_usage_attributes_device_usage_form_dict = client_usage_attributes_device_usage.from_dict(client_usage_attributes_device_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



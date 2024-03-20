# DeviceUsageAttributes

The type-specific properties of the client usage object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device&#39;s name | [optional] 
**usage_period** | [**ClientUsageAttributesUsagePeriod**](ClientUsageAttributesUsagePeriod.md) |  | [optional] 
**total_days** | **float** | The total billable device days across the usage period | [optional] 
**average_days** | **float** | The average billable device days across the usage period | [optional] 
**total_days_by_client_type** | [**DeviceUsageAttributesTotalDaysByClientType**](DeviceUsageAttributesTotalDaysByClientType.md) |  | [optional] 
**average_days_by_client_type** | [**DeviceUsageAttributesAverageDaysByClientType**](DeviceUsageAttributesAverageDaysByClientType.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_usage_attributes import DeviceUsageAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageAttributes from a JSON string
device_usage_attributes_instance = DeviceUsageAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceUsageAttributes.to_json()

# convert the object into a dict
device_usage_attributes_dict = device_usage_attributes_instance.to_dict()
# create an instance of DeviceUsageAttributes from a dict
device_usage_attributes_form_dict = device_usage_attributes.from_dict(device_usage_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



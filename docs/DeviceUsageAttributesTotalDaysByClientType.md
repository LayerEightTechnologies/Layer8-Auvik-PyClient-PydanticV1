# DeviceUsageAttributesTotalDaysByClientType

The total billable device days for across the usage period, separate by this device's owning client type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notier** | **float** | Billable devices days for the device when its client had no set client type | [optional] 
**light** | **float** | Billable devices days for the device when its client was set to Light | [optional] 
**essentials** | **float** | Billable devices days for the device when its client was set to Essentials | [optional] 
**performance** | **float** | Billable devices days for the device when its client was set to Performance | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_usage_attributes_total_days_by_client_type import DeviceUsageAttributesTotalDaysByClientType

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageAttributesTotalDaysByClientType from a JSON string
device_usage_attributes_total_days_by_client_type_instance = DeviceUsageAttributesTotalDaysByClientType.from_json(json)
# print the JSON string representation of the object
print DeviceUsageAttributesTotalDaysByClientType.to_json()

# convert the object into a dict
device_usage_attributes_total_days_by_client_type_dict = device_usage_attributes_total_days_by_client_type_instance.to_dict()
# create an instance of DeviceUsageAttributesTotalDaysByClientType from a dict
device_usage_attributes_total_days_by_client_type_form_dict = device_usage_attributes_total_days_by_client_type.from_dict(device_usage_attributes_total_days_by_client_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



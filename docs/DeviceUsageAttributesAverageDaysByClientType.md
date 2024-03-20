# DeviceUsageAttributesAverageDaysByClientType

The average billable device days for all clients across the usage period, separate by devices' owning client type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notier** | **float** | Average billable devices days for the device when its client had no set client type | [optional] 
**light** | **float** | Average billable devices days for the device when its client was set to Light | [optional] 
**essentials** | **float** | Average billable devices days for the device when its client was set to Essentials | [optional] 
**performance** | **float** | Average billable devices days for the device when its client was set to Performance | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_usage_attributes_average_days_by_client_type import DeviceUsageAttributesAverageDaysByClientType

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageAttributesAverageDaysByClientType from a JSON string
device_usage_attributes_average_days_by_client_type_instance = DeviceUsageAttributesAverageDaysByClientType.from_json(json)
# print the JSON string representation of the object
print DeviceUsageAttributesAverageDaysByClientType.to_json()

# convert the object into a dict
device_usage_attributes_average_days_by_client_type_dict = device_usage_attributes_average_days_by_client_type_instance.to_dict()
# create an instance of DeviceUsageAttributesAverageDaysByClientType from a dict
device_usage_attributes_average_days_by_client_type_form_dict = device_usage_attributes_average_days_by_client_type.from_dict(device_usage_attributes_average_days_by_client_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



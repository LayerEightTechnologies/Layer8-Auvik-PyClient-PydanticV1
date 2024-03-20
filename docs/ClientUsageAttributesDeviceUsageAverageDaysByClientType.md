# ClientUsageAttributesDeviceUsageAverageDaysByClientType

The average billable device days for this client and all of its children across the usage period, separate by devices' owning client type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notier** | **float** | Average billable devices days for devices on a client with no set client type | [optional] 
**light** | **float** | Average billable devices days for devices on a client set to Light | [optional] 
**essentials** | **float** | Average billable devices days for devices on a client set to Essentials | [optional] 
**performance** | **float** | Average billable devices days for devices on a client set to Performance | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_attributes_device_usage_average_days_by_client_type import ClientUsageAttributesDeviceUsageAverageDaysByClientType

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageAttributesDeviceUsageAverageDaysByClientType from a JSON string
client_usage_attributes_device_usage_average_days_by_client_type_instance = ClientUsageAttributesDeviceUsageAverageDaysByClientType.from_json(json)
# print the JSON string representation of the object
print ClientUsageAttributesDeviceUsageAverageDaysByClientType.to_json()

# convert the object into a dict
client_usage_attributes_device_usage_average_days_by_client_type_dict = client_usage_attributes_device_usage_average_days_by_client_type_instance.to_dict()
# create an instance of ClientUsageAttributesDeviceUsageAverageDaysByClientType from a dict
client_usage_attributes_device_usage_average_days_by_client_type_form_dict = client_usage_attributes_device_usage_average_days_by_client_type.from_dict(client_usage_attributes_device_usage_average_days_by_client_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



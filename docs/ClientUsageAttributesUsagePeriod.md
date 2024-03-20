# ClientUsageAttributesUsagePeriod

Description of the usage period that's been asked for

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Date and time the usage period starts | [optional] 
**end_date** | **str** | Date and time the usage period ends | [optional] 
**length_in_days** | **float** | Number of days in the usage period | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_attributes_usage_period import ClientUsageAttributesUsagePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageAttributesUsagePeriod from a JSON string
client_usage_attributes_usage_period_instance = ClientUsageAttributesUsagePeriod.from_json(json)
# print the JSON string representation of the object
print ClientUsageAttributesUsagePeriod.to_json()

# convert the object into a dict
client_usage_attributes_usage_period_dict = client_usage_attributes_usage_period_instance.to_dict()
# create an instance of ClientUsageAttributesUsagePeriod from a dict
client_usage_attributes_usage_period_form_dict = client_usage_attributes_usage_period.from_dict(client_usage_attributes_usage_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



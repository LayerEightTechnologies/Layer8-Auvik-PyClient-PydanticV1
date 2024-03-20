# ClientUsageAttributes

The type-specific properties of the client usage object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_prefix** | **str** | Client tenant&#39;s domain prefix/name | [optional] 
**billable_days** | **float** | Days this client (and its children) was billable for across the usage period. | [optional] 
**usage_period** | [**ClientUsageAttributesUsagePeriod**](ClientUsageAttributesUsagePeriod.md) |  | [optional] 
**device_usage** | [**ClientUsageAttributesDeviceUsage**](ClientUsageAttributesDeviceUsage.md) |  | [optional] 
**client_usage** | [**ClientUsageAttributesClientUsage**](ClientUsageAttributesClientUsage.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_attributes import ClientUsageAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageAttributes from a JSON string
client_usage_attributes_instance = ClientUsageAttributes.from_json(json)
# print the JSON string representation of the object
print ClientUsageAttributes.to_json()

# convert the object into a dict
client_usage_attributes_dict = client_usage_attributes_instance.to_dict()
# create an instance of ClientUsageAttributes from a dict
client_usage_attributes_form_dict = client_usage_attributes.from_dict(client_usage_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



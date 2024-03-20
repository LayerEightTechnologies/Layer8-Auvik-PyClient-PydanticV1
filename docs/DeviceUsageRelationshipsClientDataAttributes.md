# DeviceUsageRelationshipsClientDataAttributes

The type-specific properties of the device usage object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_prefix** | **str** | Client tenant&#39;s domain prefix/name | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_usage_relationships_client_data_attributes import DeviceUsageRelationshipsClientDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageRelationshipsClientDataAttributes from a JSON string
device_usage_relationships_client_data_attributes_instance = DeviceUsageRelationshipsClientDataAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceUsageRelationshipsClientDataAttributes.to_json()

# convert the object into a dict
device_usage_relationships_client_data_attributes_dict = device_usage_relationships_client_data_attributes_instance.to_dict()
# create an instance of DeviceUsageRelationshipsClientDataAttributes from a dict
device_usage_relationships_client_data_attributes_form_dict = device_usage_relationships_client_data_attributes.from_dict(device_usage_relationships_client_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



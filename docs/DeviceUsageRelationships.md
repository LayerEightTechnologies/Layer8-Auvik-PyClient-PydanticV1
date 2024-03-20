# DeviceUsageRelationships

Client usage object's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**DeviceUsageRelationshipsClient**](DeviceUsageRelationshipsClient.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_usage_relationships import DeviceUsageRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageRelationships from a JSON string
device_usage_relationships_instance = DeviceUsageRelationships.from_json(json)
# print the JSON string representation of the object
print DeviceUsageRelationships.to_json()

# convert the object into a dict
device_usage_relationships_dict = device_usage_relationships_instance.to_dict()
# create an instance of DeviceUsageRelationships from a dict
device_usage_relationships_form_dict = device_usage_relationships.from_dict(device_usage_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



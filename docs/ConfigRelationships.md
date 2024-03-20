# ConfigRelationships

This configurations relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**device** | [**DeviceLifecycleRelationshipsDevice**](DeviceLifecycleRelationshipsDevice.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.config_relationships import ConfigRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigRelationships from a JSON string
config_relationships_instance = ConfigRelationships.from_json(json)
# print the JSON string representation of the object
print ConfigRelationships.to_json()

# convert the object into a dict
config_relationships_dict = config_relationships_instance.to_dict()
# create an instance of ConfigRelationships from a dict
config_relationships_form_dict = config_relationships.from_dict(config_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



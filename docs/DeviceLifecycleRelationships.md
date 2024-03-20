# DeviceLifecycleRelationships

This device's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**device** | [**DeviceLifecycleRelationshipsDevice**](DeviceLifecycleRelationshipsDevice.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_lifecycle_relationships import DeviceLifecycleRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLifecycleRelationships from a JSON string
device_lifecycle_relationships_instance = DeviceLifecycleRelationships.from_json(json)
# print the JSON string representation of the object
print DeviceLifecycleRelationships.to_json()

# convert the object into a dict
device_lifecycle_relationships_dict = device_lifecycle_relationships_instance.to_dict()
# create an instance of DeviceLifecycleRelationships from a dict
device_lifecycle_relationships_form_dict = device_lifecycle_relationships.from_dict(device_lifecycle_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



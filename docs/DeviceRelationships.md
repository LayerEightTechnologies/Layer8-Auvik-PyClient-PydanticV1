# DeviceRelationships

This device's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**networks** | [**DeviceRelationshipsNetworks**](DeviceRelationshipsNetworks.md) |  | [optional] 
**device_detail** | [**DeviceRelationshipsDeviceDetail**](DeviceRelationshipsDeviceDetail.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_relationships import DeviceRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRelationships from a JSON string
device_relationships_instance = DeviceRelationships.from_json(json)
# print the JSON string representation of the object
print DeviceRelationships.to_json()

# convert the object into a dict
device_relationships_dict = device_relationships_instance.to_dict()
# create an instance of DeviceRelationships from a dict
device_relationships_form_dict = device_relationships.from_dict(device_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



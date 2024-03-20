# DeviceDetailsRelationships

This device's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**connected_devices** | [**DeviceDetailsRelationshipsConnectedDevices**](DeviceDetailsRelationshipsConnectedDevices.md) |  | [optional] 
**interfaces** | [**DeviceDetailsRelationshipsInterfaces**](DeviceDetailsRelationshipsInterfaces.md) |  | [optional] 
**configurations** | [**DeviceDetailsRelationshipsConfigurations**](DeviceDetailsRelationshipsConfigurations.md) |  | [optional] 
**components** | [**DeviceDetailsRelationshipsComponents**](DeviceDetailsRelationshipsComponents.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships import DeviceDetailsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationships from a JSON string
device_details_relationships_instance = DeviceDetailsRelationships.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationships.to_json()

# convert the object into a dict
device_details_relationships_dict = device_details_relationships_instance.to_dict()
# create an instance of DeviceDetailsRelationships from a dict
device_details_relationships_form_dict = device_details_relationships.from_dict(device_details_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeviceDetailsRelationshipsInterfaces

This device's interfaces

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeviceDetailsRelationshipsInterfacesData]**](DeviceDetailsRelationshipsInterfacesData.md) | An interface resource object | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_interfaces import DeviceDetailsRelationshipsInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsInterfaces from a JSON string
device_details_relationships_interfaces_instance = DeviceDetailsRelationshipsInterfaces.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsInterfaces.to_json()

# convert the object into a dict
device_details_relationships_interfaces_dict = device_details_relationships_interfaces_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsInterfaces from a dict
device_details_relationships_interfaces_form_dict = device_details_relationships_interfaces.from_dict(device_details_relationships_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



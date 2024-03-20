# OidRelationshipsDeviceData

A device resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This device&#39;s ID | [optional] 
**type** | **str** | The type of the object | [optional] 
**device_type** | **str** | The type of the device | [optional] 
**device_name** | **str** | The name of the device | [optional] 
**links** | [**InterfaceRelationshipsParentDeviceDataLinks**](InterfaceRelationshipsParentDeviceDataLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.oid_relationships_device_data import OidRelationshipsDeviceData

# TODO update the JSON string below
json = "{}"
# create an instance of OidRelationshipsDeviceData from a JSON string
oid_relationships_device_data_instance = OidRelationshipsDeviceData.from_json(json)
# print the JSON string representation of the object
print OidRelationshipsDeviceData.to_json()

# convert the object into a dict
oid_relationships_device_data_dict = oid_relationships_device_data_instance.to_dict()
# create an instance of OidRelationshipsDeviceData from a dict
oid_relationships_device_data_form_dict = oid_relationships_device_data.from_dict(oid_relationships_device_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



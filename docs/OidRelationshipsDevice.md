# OidRelationshipsDevice

This OID's device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OidRelationshipsDeviceData**](OidRelationshipsDeviceData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.oid_relationships_device import OidRelationshipsDevice

# TODO update the JSON string below
json = "{}"
# create an instance of OidRelationshipsDevice from a JSON string
oid_relationships_device_instance = OidRelationshipsDevice.from_json(json)
# print the JSON string representation of the object
print OidRelationshipsDevice.to_json()

# convert the object into a dict
oid_relationships_device_dict = oid_relationships_device_instance.to_dict()
# create an instance of OidRelationshipsDevice from a dict
oid_relationships_device_form_dict = oid_relationships_device.from_dict(oid_relationships_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



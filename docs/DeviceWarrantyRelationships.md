# DeviceWarrantyRelationships

This device's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_warranty_relationships import DeviceWarrantyRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceWarrantyRelationships from a JSON string
device_warranty_relationships_instance = DeviceWarrantyRelationships.from_json(json)
# print the JSON string representation of the object
print DeviceWarrantyRelationships.to_json()

# convert the object into a dict
device_warranty_relationships_dict = device_warranty_relationships_instance.to_dict()
# create an instance of DeviceWarrantyRelationships from a dict
device_warranty_relationships_form_dict = device_warranty_relationships.from_dict(device_warranty_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



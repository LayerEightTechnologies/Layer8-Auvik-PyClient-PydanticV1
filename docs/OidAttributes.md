# OidAttributes

The type-specific properties of the OID object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oid** | **str** | OID identifier | 
**oid_name** | **str** | OID name | [optional] 
**value** | **float** | OID value | [optional] 

## Example

```python
from layer8_auvik_api_client.models.oid_attributes import OidAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of OidAttributes from a JSON string
oid_attributes_instance = OidAttributes.from_json(json)
# print the JSON string representation of the object
print OidAttributes.to_json()

# convert the object into a dict
oid_attributes_dict = oid_attributes_instance.to_dict()
# create an instance of OidAttributes from a dict
oid_attributes_form_dict = oid_attributes.from_dict(oid_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TenantsDetailReadSingle

root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TenantDetailResourceObject**](TenantDetailResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenants_detail_read_single import TenantsDetailReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of TenantsDetailReadSingle from a JSON string
tenants_detail_read_single_instance = TenantsDetailReadSingle.from_json(json)
# print the JSON string representation of the object
print TenantsDetailReadSingle.to_json()

# convert the object into a dict
tenants_detail_read_single_dict = tenants_detail_read_single_instance.to_dict()
# create an instance of TenantsDetailReadSingle from a dict
tenants_detail_read_single_form_dict = tenants_detail_read_single.from_dict(tenants_detail_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



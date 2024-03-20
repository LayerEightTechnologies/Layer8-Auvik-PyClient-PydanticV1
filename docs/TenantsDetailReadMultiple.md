# TenantsDetailReadMultiple

root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TenantDetailResourceObject]**](TenantDetailResourceObject.md) | An array of resource objects, an array of resource identifier objects, or an empty array ([]), for requests that target resource collections. | [optional] 

## Example

```python
from layer8_auvik_api_client.models.tenants_detail_read_multiple import TenantsDetailReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of TenantsDetailReadMultiple from a JSON string
tenants_detail_read_multiple_instance = TenantsDetailReadMultiple.from_json(json)
# print the JSON string representation of the object
print TenantsDetailReadMultiple.to_json()

# convert the object into a dict
tenants_detail_read_multiple_dict = tenants_detail_read_multiple_instance.to_dict()
# create an instance of TenantsDetailReadMultiple from a dict
tenants_detail_read_multiple_form_dict = tenants_detail_read_multiple.from_dict(tenants_detail_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



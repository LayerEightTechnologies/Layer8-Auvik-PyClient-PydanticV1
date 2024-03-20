# UserTenantsReadMultiple

root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TenantsResourceObject]**](TenantsResourceObject.md) | An array of resource objects, an array of resource identifier objects, or an empty array ([]), for requests that target resource collections. | [optional] 

## Example

```python
from layer8_auvik_api_client.models.user_tenants_read_multiple import UserTenantsReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of UserTenantsReadMultiple from a JSON string
user_tenants_read_multiple_instance = UserTenantsReadMultiple.from_json(json)
# print the JSON string representation of the object
print UserTenantsReadMultiple.to_json()

# convert the object into a dict
user_tenants_read_multiple_dict = user_tenants_read_multiple_instance.to_dict()
# create an instance of UserTenantsReadMultiple from a dict
user_tenants_read_multiple_form_dict = user_tenants_read_multiple.from_dict(user_tenants_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



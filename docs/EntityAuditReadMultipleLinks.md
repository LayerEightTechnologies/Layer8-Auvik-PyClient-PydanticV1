# EntityAuditReadMultipleLinks

Pagination related links

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page in the data set | [optional] 
**prev** | **str** | Previous page in the data set | [optional] 
**first** | **str** | First page in the data set | [optional] 
**last** | **str** | Last page in the data set | [optional] 

## Example

```python
from layer8_auvik_api_client.models.entity_audit_read_multiple_links import EntityAuditReadMultipleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAuditReadMultipleLinks from a JSON string
entity_audit_read_multiple_links_instance = EntityAuditReadMultipleLinks.from_json(json)
# print the JSON string representation of the object
print EntityAuditReadMultipleLinks.to_json()

# convert the object into a dict
entity_audit_read_multiple_links_dict = entity_audit_read_multiple_links_instance.to_dict()
# create an instance of EntityAuditReadMultipleLinks from a dict
entity_audit_read_multiple_links_form_dict = entity_audit_read_multiple_links.from_dict(entity_audit_read_multiple_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



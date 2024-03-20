# AuditAttributes

The type-specific properties of the audit object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | The user name associated to this audit log | 
**category** | **str** | What service is taking/took this audited action | 
**action** | **str** | What action is being performed | 
**direction** | **str** | Whether is request is being made into or out of the entity&#39;s client | 
**status** | **str** | State of the audited action | 
**cause** | **str** | Reason the audited action is in its current state | 
**data** | **str** | Tertiary data related to the audited action | 
**date_started** | **str** | When this audited action was started | 
**last_active** | **str** | When this audited action was last active | 

## Example

```python
from layer8_auvik_api_client.models.audit_attributes import AuditAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AuditAttributes from a JSON string
audit_attributes_instance = AuditAttributes.from_json(json)
# print the JSON string representation of the object
print AuditAttributes.to_json()

# convert the object into a dict
audit_attributes_dict = audit_attributes_instance.to_dict()
# create an instance of AuditAttributes from a dict
audit_attributes_form_dict = audit_attributes.from_dict(audit_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



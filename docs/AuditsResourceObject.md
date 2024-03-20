# AuditsResourceObject

The template for a resource object representing an audit log

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for this audit | [optional] 
**attributes** | [**AuditAttributes**](AuditAttributes.md) |  | [optional] 
**relationships** | [**AuditRelationships**](AuditRelationships.md) |  | [optional] 
**links** | [**AuditsResourceObjectLinks**](AuditsResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.audits_resource_object import AuditsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of AuditsResourceObject from a JSON string
audits_resource_object_instance = AuditsResourceObject.from_json(json)
# print the JSON string representation of the object
print AuditsResourceObject.to_json()

# convert the object into a dict
audits_resource_object_dict = audits_resource_object_instance.to_dict()
# create an instance of AuditsResourceObject from a dict
audits_resource_object_form_dict = audits_resource_object.from_dict(audits_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



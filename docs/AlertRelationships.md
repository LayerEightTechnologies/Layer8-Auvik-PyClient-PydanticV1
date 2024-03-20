# AlertRelationships

This interface's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**related_alert** | [**AlertRelationshipsRelatedAlert**](AlertRelationshipsRelatedAlert.md) |  | [optional] 
**entity** | [**AlertRelationshipsEntity**](AlertRelationshipsEntity.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_relationships import AlertRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRelationships from a JSON string
alert_relationships_instance = AlertRelationships.from_json(json)
# print the JSON string representation of the object
print AlertRelationships.to_json()

# convert the object into a dict
alert_relationships_dict = alert_relationships_instance.to_dict()
# create an instance of AlertRelationships from a dict
alert_relationships_form_dict = alert_relationships.from_dict(alert_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



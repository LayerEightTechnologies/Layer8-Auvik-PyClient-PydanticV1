# AlertRelationshipsEntity

This entity associated to the alert message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlertRelationshipsEntityData**](AlertRelationshipsEntityData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_relationships_entity import AlertRelationshipsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRelationshipsEntity from a JSON string
alert_relationships_entity_instance = AlertRelationshipsEntity.from_json(json)
# print the JSON string representation of the object
print AlertRelationshipsEntity.to_json()

# convert the object into a dict
alert_relationships_entity_dict = alert_relationships_entity_instance.to_dict()
# create an instance of AlertRelationshipsEntity from a dict
alert_relationships_entity_form_dict = alert_relationships_entity.from_dict(alert_relationships_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



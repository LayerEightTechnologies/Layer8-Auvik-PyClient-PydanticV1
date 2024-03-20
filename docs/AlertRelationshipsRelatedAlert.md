# AlertRelationshipsRelatedAlert

The related alert linked to the current one

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlertRelationshipsRelatedAlertData**](AlertRelationshipsRelatedAlertData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_relationships_related_alert import AlertRelationshipsRelatedAlert

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRelationshipsRelatedAlert from a JSON string
alert_relationships_related_alert_instance = AlertRelationshipsRelatedAlert.from_json(json)
# print the JSON string representation of the object
print AlertRelationshipsRelatedAlert.to_json()

# convert the object into a dict
alert_relationships_related_alert_dict = alert_relationships_related_alert_instance.to_dict()
# create an instance of AlertRelationshipsRelatedAlert from a dict
alert_relationships_related_alert_form_dict = alert_relationships_related_alert.from_dict(alert_relationships_related_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



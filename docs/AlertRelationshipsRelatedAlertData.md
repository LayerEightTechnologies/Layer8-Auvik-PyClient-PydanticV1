# AlertRelationshipsRelatedAlertData

This alert associated to the related alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the api | [optional] 
**id** | **str** | The unique identifier for this alert | [optional] 
**attributes** | [**AlertRelationshipsRelatedAlertDataAttributes**](AlertRelationshipsRelatedAlertDataAttributes.md) |  | [optional] 
**links** | [**AlertRelationshipsRelatedAlertDataLinks**](AlertRelationshipsRelatedAlertDataLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_relationships_related_alert_data import AlertRelationshipsRelatedAlertData

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRelationshipsRelatedAlertData from a JSON string
alert_relationships_related_alert_data_instance = AlertRelationshipsRelatedAlertData.from_json(json)
# print the JSON string representation of the object
print AlertRelationshipsRelatedAlertData.to_json()

# convert the object into a dict
alert_relationships_related_alert_data_dict = alert_relationships_related_alert_data_instance.to_dict()
# create an instance of AlertRelationshipsRelatedAlertData from a dict
alert_relationships_related_alert_data_form_dict = alert_relationships_related_alert_data.from_dict(alert_relationships_related_alert_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



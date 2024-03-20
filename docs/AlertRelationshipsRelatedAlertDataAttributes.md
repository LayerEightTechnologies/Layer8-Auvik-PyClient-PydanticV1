# AlertRelationshipsRelatedAlertDataAttributes

The attribute of the related alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of related alert | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_relationships_related_alert_data_attributes import AlertRelationshipsRelatedAlertDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRelationshipsRelatedAlertDataAttributes from a JSON string
alert_relationships_related_alert_data_attributes_instance = AlertRelationshipsRelatedAlertDataAttributes.from_json(json)
# print the JSON string representation of the object
print AlertRelationshipsRelatedAlertDataAttributes.to_json()

# convert the object into a dict
alert_relationships_related_alert_data_attributes_dict = alert_relationships_related_alert_data_attributes_instance.to_dict()
# create an instance of AlertRelationshipsRelatedAlertDataAttributes from a dict
alert_relationships_related_alert_data_attributes_form_dict = alert_relationships_related_alert_data_attributes.from_dict(alert_relationships_related_alert_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



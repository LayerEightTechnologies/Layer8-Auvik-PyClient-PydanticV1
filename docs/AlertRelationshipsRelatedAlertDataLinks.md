# AlertRelationshipsRelatedAlertDataLinks

Links relating to this interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this interface&#39;s dashboard in the Auvik UI | [optional] 
**var_self** | **str** | Link to this alert info | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_relationships_related_alert_data_links import AlertRelationshipsRelatedAlertDataLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRelationshipsRelatedAlertDataLinks from a JSON string
alert_relationships_related_alert_data_links_instance = AlertRelationshipsRelatedAlertDataLinks.from_json(json)
# print the JSON string representation of the object
print AlertRelationshipsRelatedAlertDataLinks.to_json()

# convert the object into a dict
alert_relationships_related_alert_data_links_dict = alert_relationships_related_alert_data_links_instance.to_dict()
# create an instance of AlertRelationshipsRelatedAlertDataLinks from a dict
alert_relationships_related_alert_data_links_form_dict = alert_relationships_related_alert_data_links.from_dict(alert_relationships_related_alert_data_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



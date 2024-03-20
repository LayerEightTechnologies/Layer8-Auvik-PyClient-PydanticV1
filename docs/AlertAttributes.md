# AlertAttributes

The type-specific properties of the alerts object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This alert&#39;s name | 
**severity** | **str** | This severity of the alert message | 
**status** | **str** | High level description of this alert&#39;s status | 
**alert_definition_id** | **str** | Alert Definition ID linked to Alert type | [optional] 
**specification_id** | **str** | Specification ID linked to Alert type. Use alertDefinitionId instead | [optional] 
**detected_on** | **str** | The date time of the alert&#39;s message was detected | 
**description** | **str** | This description of the alert | 
**dismissed** | **bool** | Whether the alert has been dismissed or not | 
**dispatched** | **bool** | Whether the alert has been dispatched or not | 
**external_ticket** | [**List[AlertAttributesExternalTicket]**](AlertAttributesExternalTicket.md) | The external ticket list associated to current alert message | 

## Example

```python
from layer8_auvik_api_client.models.alert_attributes import AlertAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AlertAttributes from a JSON string
alert_attributes_instance = AlertAttributes.from_json(json)
# print the JSON string representation of the object
print AlertAttributes.to_json()

# convert the object into a dict
alert_attributes_dict = alert_attributes_instance.to_dict()
# create an instance of AlertAttributes from a dict
alert_attributes_form_dict = alert_attributes.from_dict(alert_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



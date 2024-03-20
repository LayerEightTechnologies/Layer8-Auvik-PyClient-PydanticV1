# AlertAttributesExternalTicket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the external ticket | [optional] 
**system** | **str** | The system of external ticket | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_attributes_external_ticket import AlertAttributesExternalTicket

# TODO update the JSON string below
json = "{}"
# create an instance of AlertAttributesExternalTicket from a JSON string
alert_attributes_external_ticket_instance = AlertAttributesExternalTicket.from_json(json)
# print the JSON string representation of the object
print AlertAttributesExternalTicket.to_json()

# convert the object into a dict
alert_attributes_external_ticket_dict = alert_attributes_external_ticket_instance.to_dict()
# create an instance of AlertAttributesExternalTicket from a dict
alert_attributes_external_ticket_form_dict = alert_attributes_external_ticket.from_dict(alert_attributes_external_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



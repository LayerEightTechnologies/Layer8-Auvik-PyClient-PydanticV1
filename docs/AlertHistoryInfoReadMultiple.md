# AlertHistoryInfoReadMultiple

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlertsResourceObject]**](AlertsResourceObject.md) |  | [optional] 
**links** | [**AlertHistoryInfoReadMultipleLinks**](AlertHistoryInfoReadMultipleLinks.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_history_info_read_multiple import AlertHistoryInfoReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of AlertHistoryInfoReadMultiple from a JSON string
alert_history_info_read_multiple_instance = AlertHistoryInfoReadMultiple.from_json(json)
# print the JSON string representation of the object
print AlertHistoryInfoReadMultiple.to_json()

# convert the object into a dict
alert_history_info_read_multiple_dict = alert_history_info_read_multiple_instance.to_dict()
# create an instance of AlertHistoryInfoReadMultiple from a dict
alert_history_info_read_multiple_form_dict = alert_history_info_read_multiple.from_dict(alert_history_info_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



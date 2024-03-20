# AlertHistoryInfoReadSingle

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlertsResourceObject**](AlertsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_history_info_read_single import AlertHistoryInfoReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of AlertHistoryInfoReadSingle from a JSON string
alert_history_info_read_single_instance = AlertHistoryInfoReadSingle.from_json(json)
# print the JSON string representation of the object
print AlertHistoryInfoReadSingle.to_json()

# convert the object into a dict
alert_history_info_read_single_dict = alert_history_info_read_single_instance.to_dict()
# create an instance of AlertHistoryInfoReadSingle from a dict
alert_history_info_read_single_form_dict = alert_history_info_read_single.from_dict(alert_history_info_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



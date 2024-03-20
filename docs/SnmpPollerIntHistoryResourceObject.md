# SnmpPollerIntHistoryResourceObject

The template for a resource object representing the history of a Integer SNMP Poller Setting's values

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for a set of history SNMP Poller Setting&#39;s values | [optional] 
**type** | **str** | The type of object in the API | [optional] 
**attributes** | [**SnmpPollerIntHistoryAttributes**](SnmpPollerIntHistoryAttributes.md) |  | [optional] 
**relationships** | [**SnmpPollerIntHistoryRelationships**](SnmpPollerIntHistoryRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_int_history_resource_object import SnmpPollerIntHistoryResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerIntHistoryResourceObject from a JSON string
snmp_poller_int_history_resource_object_instance = SnmpPollerIntHistoryResourceObject.from_json(json)
# print the JSON string representation of the object
print SnmpPollerIntHistoryResourceObject.to_json()

# convert the object into a dict
snmp_poller_int_history_resource_object_dict = snmp_poller_int_history_resource_object_instance.to_dict()
# create an instance of SnmpPollerIntHistoryResourceObject from a dict
snmp_poller_int_history_resource_object_form_dict = snmp_poller_int_history_resource_object.from_dict(snmp_poller_int_history_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



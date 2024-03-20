# SnmpPollerSettingsReadLinks

Pagination related links

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page in the data set | [optional] 
**prev** | **str** | Previous page in the data set | [optional] 
**first** | **str** | First page in the data set | [optional] 
**last** | **str** | Last page in the data set | [optional] 

## Example

```python
from layer8_auvik_api_client.models.snmp_poller_settings_read_links import SnmpPollerSettingsReadLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpPollerSettingsReadLinks from a JSON string
snmp_poller_settings_read_links_instance = SnmpPollerSettingsReadLinks.from_json(json)
# print the JSON string representation of the object
print SnmpPollerSettingsReadLinks.to_json()

# convert the object into a dict
snmp_poller_settings_read_links_dict = snmp_poller_settings_read_links_instance.to_dict()
# create an instance of SnmpPollerSettingsReadLinks from a dict
snmp_poller_settings_read_links_form_dict = snmp_poller_settings_read_links.from_dict(snmp_poller_settings_read_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



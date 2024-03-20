# InterfaceAttributes

The type-specific properties of the interfaces object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_name** | **str** | This interface&#39;s name | 
**interface_type** | **str** | This interface&#39;s type | 
**mac_address** | **str** | MAC address | 
**negotiated_speed** | **str** | Negotiated speed | 
**duplex** | **str** | Duplex mode of this interface | 
**custom_connections** | **bool** | Whether this interface allows custom connections | 
**ip_addresses** | **List[str]** | This interface&#39;s IP addresses | 
**operational_status** | **str** | This interface&#39;s operational status | 
**admin_status** | **bool** | Whether this interface is enabled | 
**last_modified** | **str** | When one of this interface&#39;s attributes was last modified | 

## Example

```python
from layer8_auvik_api_client.models.interface_attributes import InterfaceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceAttributes from a JSON string
interface_attributes_instance = InterfaceAttributes.from_json(json)
# print the JSON string representation of the object
print InterfaceAttributes.to_json()

# convert the object into a dict
interface_attributes_dict = interface_attributes_instance.to_dict()
# create an instance of InterfaceAttributes from a dict
interface_attributes_form_dict = interface_attributes.from_dict(interface_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



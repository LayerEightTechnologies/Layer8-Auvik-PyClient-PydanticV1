# AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes

This wireless client's attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_type** | **str** | What type of device it is | 
**device_name** | **str** |  | 
**ssid** | **str** | The wireless client&#39;s SSID | 
**channel** | **str** | The wireless client&#39;s radio channel | 
**rssi** | **str** | The wireless&#39;s clients RSSI | 

## Example

```python
from layer8_auvik_api_client.models.access_point_all_of_relationships_all_of_wireless_clients_inner_attributes import AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes from a JSON string
access_point_all_of_relationships_all_of_wireless_clients_inner_attributes_instance = AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes.from_json(json)
# print the JSON string representation of the object
print AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes.to_json()

# convert the object into a dict
access_point_all_of_relationships_all_of_wireless_clients_inner_attributes_dict = access_point_all_of_relationships_all_of_wireless_clients_inner_attributes_instance.to_dict()
# create an instance of AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes from a dict
access_point_all_of_relationships_all_of_wireless_clients_inner_attributes_form_dict = access_point_all_of_relationships_all_of_wireless_clients_inner_attributes.from_dict(access_point_all_of_relationships_all_of_wireless_clients_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



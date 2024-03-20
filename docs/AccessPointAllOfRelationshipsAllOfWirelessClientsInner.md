# AccessPointAllOfRelationshipsAllOfWirelessClientsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This wireless client&#39;s ID | [optional] 
**type** | **str** | Resource type of this wireless client | [optional] 
**attributes** | [**AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes**](AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes.md) |  | [optional] 
**links** | [**ControllerAllOfRelationshipsAllOfAccessPointsInnerLinks**](ControllerAllOfRelationshipsAllOfAccessPointsInnerLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.access_point_all_of_relationships_all_of_wireless_clients_inner import AccessPointAllOfRelationshipsAllOfWirelessClientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPointAllOfRelationshipsAllOfWirelessClientsInner from a JSON string
access_point_all_of_relationships_all_of_wireless_clients_inner_instance = AccessPointAllOfRelationshipsAllOfWirelessClientsInner.from_json(json)
# print the JSON string representation of the object
print AccessPointAllOfRelationshipsAllOfWirelessClientsInner.to_json()

# convert the object into a dict
access_point_all_of_relationships_all_of_wireless_clients_inner_dict = access_point_all_of_relationships_all_of_wireless_clients_inner_instance.to_dict()
# create an instance of AccessPointAllOfRelationshipsAllOfWirelessClientsInner from a dict
access_point_all_of_relationships_all_of_wireless_clients_inner_form_dict = access_point_all_of_relationships_all_of_wireless_clients_inner.from_dict(access_point_all_of_relationships_all_of_wireless_clients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AccessPointAllOfRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**networks** | [**DeviceRelationshipsNetworks**](DeviceRelationshipsNetworks.md) |  | [optional] 
**device_detail** | [**DeviceRelationshipsDeviceDetail**](DeviceRelationshipsDeviceDetail.md) |  | [optional] 
**wireless_clients** | [**List[AccessPointAllOfRelationshipsAllOfWirelessClientsInner]**](AccessPointAllOfRelationshipsAllOfWirelessClientsInner.md) | List of wireless clients associated to this controller | [optional] 

## Example

```python
from layer8_auvik_api_client.models.access_point_all_of_relationships import AccessPointAllOfRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPointAllOfRelationships from a JSON string
access_point_all_of_relationships_instance = AccessPointAllOfRelationships.from_json(json)
# print the JSON string representation of the object
print AccessPointAllOfRelationships.to_json()

# convert the object into a dict
access_point_all_of_relationships_dict = access_point_all_of_relationships_instance.to_dict()
# create an instance of AccessPointAllOfRelationships from a dict
access_point_all_of_relationships_form_dict = access_point_all_of_relationships.from_dict(access_point_all_of_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



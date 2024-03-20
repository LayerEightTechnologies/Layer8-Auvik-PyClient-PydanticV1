# ControllerAllOfRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**networks** | [**DeviceRelationshipsNetworks**](DeviceRelationshipsNetworks.md) |  | [optional] 
**device_detail** | [**DeviceRelationshipsDeviceDetail**](DeviceRelationshipsDeviceDetail.md) |  | [optional] 
**access_points** | [**List[ControllerAllOfRelationshipsAllOfAccessPointsInner]**](ControllerAllOfRelationshipsAllOfAccessPointsInner.md) | List of access points associated to this controller | [optional] 

## Example

```python
from layer8_auvik_api_client.models.controller_all_of_relationships import ControllerAllOfRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerAllOfRelationships from a JSON string
controller_all_of_relationships_instance = ControllerAllOfRelationships.from_json(json)
# print the JSON string representation of the object
print ControllerAllOfRelationships.to_json()

# convert the object into a dict
controller_all_of_relationships_dict = controller_all_of_relationships_instance.to_dict()
# create an instance of ControllerAllOfRelationships from a dict
controller_all_of_relationships_form_dict = controller_all_of_relationships.from_dict(controller_all_of_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



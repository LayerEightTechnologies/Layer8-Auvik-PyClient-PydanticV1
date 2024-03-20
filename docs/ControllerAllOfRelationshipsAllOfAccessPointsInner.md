# ControllerAllOfRelationshipsAllOfAccessPointsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The AP&#39;s device ID | [optional] 
**type** | **str** | This access point&#39;s device type | [optional] 
**attributes** | [**ControllerAllOfRelationshipsAllOfAccessPointsInnerAttributes**](ControllerAllOfRelationshipsAllOfAccessPointsInnerAttributes.md) |  | [optional] 
**links** | [**ControllerAllOfRelationshipsAllOfAccessPointsInnerLinks**](ControllerAllOfRelationshipsAllOfAccessPointsInnerLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.controller_all_of_relationships_all_of_access_points_inner import ControllerAllOfRelationshipsAllOfAccessPointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerAllOfRelationshipsAllOfAccessPointsInner from a JSON string
controller_all_of_relationships_all_of_access_points_inner_instance = ControllerAllOfRelationshipsAllOfAccessPointsInner.from_json(json)
# print the JSON string representation of the object
print ControllerAllOfRelationshipsAllOfAccessPointsInner.to_json()

# convert the object into a dict
controller_all_of_relationships_all_of_access_points_inner_dict = controller_all_of_relationships_all_of_access_points_inner_instance.to_dict()
# create an instance of ControllerAllOfRelationshipsAllOfAccessPointsInner from a dict
controller_all_of_relationships_all_of_access_points_inner_form_dict = controller_all_of_relationships_all_of_access_points_inner.from_dict(controller_all_of_relationships_all_of_access_points_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



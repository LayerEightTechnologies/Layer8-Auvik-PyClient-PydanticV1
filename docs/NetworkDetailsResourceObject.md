# NetworkDetailsResourceObject

The template for a resource object representing an Auvik network's extra details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a network | [optional] 
**attributes** | [**NetworkDetailsAttributes**](NetworkDetailsAttributes.md) |  | [optional] 
**relationships** | [**NetworkDetailsRelationships**](NetworkDetailsRelationships.md) |  | [optional] 
**links** | [**NetworkDetailsResourceObjectLinks**](NetworkDetailsResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_details_resource_object import NetworkDetailsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDetailsResourceObject from a JSON string
network_details_resource_object_instance = NetworkDetailsResourceObject.from_json(json)
# print the JSON string representation of the object
print NetworkDetailsResourceObject.to_json()

# convert the object into a dict
network_details_resource_object_dict = network_details_resource_object_instance.to_dict()
# create an instance of NetworkDetailsResourceObject from a dict
network_details_resource_object_form_dict = network_details_resource_object.from_dict(network_details_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NetworksResourceObject

The template for a resource object representing an Auvik network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for this network | [optional] 
**attributes** | [**NetworkAttributes**](NetworkAttributes.md) |  | [optional] 
**relationships** | [**NetworkRelationships**](NetworkRelationships.md) |  | [optional] 
**links** | [**NetworksResourceObjectLinks**](NetworksResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.networks_resource_object import NetworksResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksResourceObject from a JSON string
networks_resource_object_instance = NetworksResourceObject.from_json(json)
# print the JSON string representation of the object
print NetworksResourceObject.to_json()

# convert the object into a dict
networks_resource_object_dict = networks_resource_object_instance.to_dict()
# create an instance of NetworksResourceObject from a dict
networks_resource_object_form_dict = networks_resource_object.from_dict(networks_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



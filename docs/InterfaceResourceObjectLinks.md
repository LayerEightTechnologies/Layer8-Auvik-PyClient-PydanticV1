# InterfaceResourceObjectLinks

List of links relating to this interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this interface&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this set of interface info | [optional] 

## Example

```python
from layer8_auvik_api_client.models.interface_resource_object_links import InterfaceResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceResourceObjectLinks from a JSON string
interface_resource_object_links_instance = InterfaceResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print InterfaceResourceObjectLinks.to_json()

# convert the object into a dict
interface_resource_object_links_dict = interface_resource_object_links_instance.to_dict()
# create an instance of InterfaceResourceObjectLinks from a dict
interface_resource_object_links_form_dict = interface_resource_object_links.from_dict(interface_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



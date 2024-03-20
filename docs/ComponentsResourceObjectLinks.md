# ComponentsResourceObjectLinks

List of links relating to this component

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this component&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this component | [optional] 

## Example

```python
from layer8_auvik_api_client.models.components_resource_object_links import ComponentsResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentsResourceObjectLinks from a JSON string
components_resource_object_links_instance = ComponentsResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print ComponentsResourceObjectLinks.to_json()

# convert the object into a dict
components_resource_object_links_dict = components_resource_object_links_instance.to_dict()
# create an instance of ComponentsResourceObjectLinks from a dict
components_resource_object_links_form_dict = components_resource_object_links.from_dict(components_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



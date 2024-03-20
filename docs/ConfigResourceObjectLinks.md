# ConfigResourceObjectLinks

List of links relating to this configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this configuration in Auvik dashboard | [optional] 
**var_self** | **str** | Link to this configuration | [optional] 

## Example

```python
from layer8_auvik_api_client.models.config_resource_object_links import ConfigResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigResourceObjectLinks from a JSON string
config_resource_object_links_instance = ConfigResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print ConfigResourceObjectLinks.to_json()

# convert the object into a dict
config_resource_object_links_dict = config_resource_object_links_instance.to_dict()
# create an instance of ConfigResourceObjectLinks from a dict
config_resource_object_links_form_dict = config_resource_object_links.from_dict(config_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



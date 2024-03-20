# NetworksResourceObjectLinks

List of links relating to this network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this network&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this set of network info | [optional] 

## Example

```python
from layer8_auvik_api_client.models.networks_resource_object_links import NetworksResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksResourceObjectLinks from a JSON string
networks_resource_object_links_instance = NetworksResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print NetworksResourceObjectLinks.to_json()

# convert the object into a dict
networks_resource_object_links_dict = networks_resource_object_links_instance.to_dict()
# create an instance of NetworksResourceObjectLinks from a dict
networks_resource_object_links_form_dict = networks_resource_object_links.from_dict(networks_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



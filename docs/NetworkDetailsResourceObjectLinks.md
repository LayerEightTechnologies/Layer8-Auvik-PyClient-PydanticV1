# NetworkDetailsResourceObjectLinks

List of links relating to this network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this network&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this set of network details | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_details_resource_object_links import NetworkDetailsResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDetailsResourceObjectLinks from a JSON string
network_details_resource_object_links_instance = NetworkDetailsResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print NetworkDetailsResourceObjectLinks.to_json()

# convert the object into a dict
network_details_resource_object_links_dict = network_details_resource_object_links_instance.to_dict()
# create an instance of NetworkDetailsResourceObjectLinks from a dict
network_details_resource_object_links_form_dict = network_details_resource_object_links.from_dict(network_details_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



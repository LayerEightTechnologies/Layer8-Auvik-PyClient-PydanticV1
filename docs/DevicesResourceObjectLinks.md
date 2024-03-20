# DevicesResourceObjectLinks

List of links relating to this device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this device&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this device | [optional] 

## Example

```python
from layer8_auvik_api_client.models.devices_resource_object_links import DevicesResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesResourceObjectLinks from a JSON string
devices_resource_object_links_instance = DevicesResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print DevicesResourceObjectLinks.to_json()

# convert the object into a dict
devices_resource_object_links_dict = devices_resource_object_links_instance.to_dict()
# create an instance of DevicesResourceObjectLinks from a dict
devices_resource_object_links_form_dict = devices_resource_object_links.from_dict(devices_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



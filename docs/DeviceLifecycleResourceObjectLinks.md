# DeviceLifecycleResourceObjectLinks

List of links relating to this device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this device&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this device lifecyle record | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_lifecycle_resource_object_links import DeviceLifecycleResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLifecycleResourceObjectLinks from a JSON string
device_lifecycle_resource_object_links_instance = DeviceLifecycleResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print DeviceLifecycleResourceObjectLinks.to_json()

# convert the object into a dict
device_lifecycle_resource_object_links_dict = device_lifecycle_resource_object_links_instance.to_dict()
# create an instance of DeviceLifecycleResourceObjectLinks from a dict
device_lifecycle_resource_object_links_form_dict = device_lifecycle_resource_object_links.from_dict(device_lifecycle_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



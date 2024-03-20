# DeviceUsageResourceObjectLinks

Links relating to this client's usage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_record** | **str** | Link to this device&#39;s record in the Device Info API | [optional] 
**var_self** | **str** | Link to this device&#39;s usage in the Usage API | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_usage_resource_object_links import DeviceUsageResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageResourceObjectLinks from a JSON string
device_usage_resource_object_links_instance = DeviceUsageResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print DeviceUsageResourceObjectLinks.to_json()

# convert the object into a dict
device_usage_resource_object_links_dict = device_usage_resource_object_links_instance.to_dict()
# create an instance of DeviceUsageResourceObjectLinks from a dict
device_usage_resource_object_links_form_dict = device_usage_resource_object_links.from_dict(device_usage_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



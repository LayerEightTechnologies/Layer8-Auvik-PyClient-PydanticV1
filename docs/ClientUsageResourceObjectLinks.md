# ClientUsageResourceObjectLinks

Links relating to this client's usage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to the billing usage dashboard in the Auvik UI. | [optional] 
**tenant_record** | **str** | Link to this client&#39;s record in the Tenants API | [optional] 
**var_self** | **str** | Link to this client&#39;s usage in the Usage API | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_resource_object_links import ClientUsageResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageResourceObjectLinks from a JSON string
client_usage_resource_object_links_instance = ClientUsageResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print ClientUsageResourceObjectLinks.to_json()

# convert the object into a dict
client_usage_resource_object_links_dict = client_usage_resource_object_links_instance.to_dict()
# create an instance of ClientUsageResourceObjectLinks from a dict
client_usage_resource_object_links_form_dict = client_usage_resource_object_links.from_dict(client_usage_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AlertsResourceObjectLinks

List of links relating to this alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this alert&#39;s dashboard in the Auvik UI | [optional] 
**var_self** | **str** | Link to this alert | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alerts_resource_object_links import AlertsResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsResourceObjectLinks from a JSON string
alerts_resource_object_links_instance = AlertsResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print AlertsResourceObjectLinks.to_json()

# convert the object into a dict
alerts_resource_object_links_dict = alerts_resource_object_links_instance.to_dict()
# create an instance of AlertsResourceObjectLinks from a dict
alerts_resource_object_links_form_dict = alerts_resource_object_links.from_dict(alerts_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



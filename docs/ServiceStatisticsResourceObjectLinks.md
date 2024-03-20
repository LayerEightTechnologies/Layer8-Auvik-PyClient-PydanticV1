# ServiceStatisticsResourceObjectLinks

Links relating to the service statistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this service&#39;s record in the Service Info API | [optional] 
**var_self** | **str** | Link used to get this result set | [optional] 

## Example

```python
from layer8_auvik_api_client.models.service_statistics_resource_object_links import ServiceStatisticsResourceObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatisticsResourceObjectLinks from a JSON string
service_statistics_resource_object_links_instance = ServiceStatisticsResourceObjectLinks.from_json(json)
# print the JSON string representation of the object
print ServiceStatisticsResourceObjectLinks.to_json()

# convert the object into a dict
service_statistics_resource_object_links_dict = service_statistics_resource_object_links_instance.to_dict()
# create an instance of ServiceStatisticsResourceObjectLinks from a dict
service_statistics_resource_object_links_form_dict = service_statistics_resource_object_links.from_dict(service_statistics_resource_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



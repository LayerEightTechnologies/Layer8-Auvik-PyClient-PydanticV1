# ComponentInfoReadMultipleLinks

Pagination related links

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page in the data set | [optional] 
**prev** | **str** | Previous page in the data set | [optional] 
**first** | **str** | First page in the data set | [optional] 
**last** | **str** | Last page in the data set | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_info_read_multiple_links import ComponentInfoReadMultipleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentInfoReadMultipleLinks from a JSON string
component_info_read_multiple_links_instance = ComponentInfoReadMultipleLinks.from_json(json)
# print the JSON string representation of the object
print ComponentInfoReadMultipleLinks.to_json()

# convert the object into a dict
component_info_read_multiple_links_dict = component_info_read_multiple_links_instance.to_dict()
# create an instance of ComponentInfoReadMultipleLinks from a dict
component_info_read_multiple_links_form_dict = component_info_read_multiple_links.from_dict(component_info_read_multiple_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



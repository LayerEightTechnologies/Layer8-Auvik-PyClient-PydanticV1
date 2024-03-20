# NetworkDetailsReadMultipleLinks

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
from layer8_auvik_api_client.models.network_details_read_multiple_links import NetworkDetailsReadMultipleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDetailsReadMultipleLinks from a JSON string
network_details_read_multiple_links_instance = NetworkDetailsReadMultipleLinks.from_json(json)
# print the JSON string representation of the object
print NetworkDetailsReadMultipleLinks.to_json()

# convert the object into a dict
network_details_read_multiple_links_dict = network_details_read_multiple_links_instance.to_dict()
# create an instance of NetworkDetailsReadMultipleLinks from a dict
network_details_read_multiple_links_form_dict = network_details_read_multiple_links.from_dict(network_details_read_multiple_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



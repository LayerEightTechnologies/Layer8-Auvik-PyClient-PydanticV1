# NetworkInfoReadMultiple

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NetworksResourceObject]**](NetworksResourceObject.md) |  | [optional] 
**included** | [**List[NetworkDetailsResourceObject]**](NetworkDetailsResourceObject.md) |  | [optional] 
**links** | [**NetworkInfoReadMultipleLinks**](NetworkInfoReadMultipleLinks.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_info_read_multiple import NetworkInfoReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInfoReadMultiple from a JSON string
network_info_read_multiple_instance = NetworkInfoReadMultiple.from_json(json)
# print the JSON string representation of the object
print NetworkInfoReadMultiple.to_json()

# convert the object into a dict
network_info_read_multiple_dict = network_info_read_multiple_instance.to_dict()
# create an instance of NetworkInfoReadMultiple from a dict
network_info_read_multiple_form_dict = network_info_read_multiple.from_dict(network_info_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



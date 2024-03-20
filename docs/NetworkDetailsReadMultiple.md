# NetworkDetailsReadMultiple

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NetworkDetailsResourceObject]**](NetworkDetailsResourceObject.md) |  | [optional] 
**links** | [**NetworkDetailsReadMultipleLinks**](NetworkDetailsReadMultipleLinks.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_details_read_multiple import NetworkDetailsReadMultiple

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDetailsReadMultiple from a JSON string
network_details_read_multiple_instance = NetworkDetailsReadMultiple.from_json(json)
# print the JSON string representation of the object
print NetworkDetailsReadMultiple.to_json()

# convert the object into a dict
network_details_read_multiple_dict = network_details_read_multiple_instance.to_dict()
# create an instance of NetworkDetailsReadMultiple from a dict
network_details_read_multiple_form_dict = network_details_read_multiple.from_dict(network_details_read_multiple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



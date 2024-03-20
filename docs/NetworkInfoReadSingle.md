# NetworkInfoReadSingle

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NetworksResourceObject**](NetworksResourceObject.md) |  | [optional] 
**included** | [**List[NetworkDetailsResourceObject]**](NetworkDetailsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_info_read_single import NetworkInfoReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInfoReadSingle from a JSON string
network_info_read_single_instance = NetworkInfoReadSingle.from_json(json)
# print the JSON string representation of the object
print NetworkInfoReadSingle.to_json()

# convert the object into a dict
network_info_read_single_dict = network_info_read_single_instance.to_dict()
# create an instance of NetworkInfoReadSingle from a dict
network_info_read_single_form_dict = network_info_read_single.from_dict(network_info_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NetworkDetailsReadSingle

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NetworkDetailsResourceObject**](NetworkDetailsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_details_read_single import NetworkDetailsReadSingle

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDetailsReadSingle from a JSON string
network_details_read_single_instance = NetworkDetailsReadSingle.from_json(json)
# print the JSON string representation of the object
print NetworkDetailsReadSingle.to_json()

# convert the object into a dict
network_details_read_single_dict = network_details_read_single_instance.to_dict()
# create an instance of NetworkDetailsReadSingle from a dict
network_details_read_single_form_dict = network_details_read_single.from_dict(network_details_read_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



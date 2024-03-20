# EndpointStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the endpoint | [optional] 
**ip_address** | **str** | IP Address of the endpoint | [optional] 
**stats** | [**List[StatItem]**](StatItem.md) | The list of statistics reported for the endpoint | [optional] 

## Example

```python
from layer8_auvik_api_client.models.endpoint_stats import EndpointStats

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointStats from a JSON string
endpoint_stats_instance = EndpointStats.from_json(json)
# print the JSON string representation of the object
print EndpointStats.to_json()

# convert the object into a dict
endpoint_stats_dict = endpoint_stats_instance.to_dict()
# create an instance of EndpointStats from a dict
endpoint_stats_form_dict = endpoint_stats.from_dict(endpoint_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



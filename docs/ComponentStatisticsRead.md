# ComponentStatisticsRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ComponentStatisticsResourceObject**](ComponentStatisticsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_statistics_read import ComponentStatisticsRead

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentStatisticsRead from a JSON string
component_statistics_read_instance = ComponentStatisticsRead.from_json(json)
# print the JSON string representation of the object
print ComponentStatisticsRead.to_json()

# convert the object into a dict
component_statistics_read_dict = component_statistics_read_instance.to_dict()
# create an instance of ComponentStatisticsRead from a dict
component_statistics_read_form_dict = component_statistics_read.from_dict(component_statistics_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



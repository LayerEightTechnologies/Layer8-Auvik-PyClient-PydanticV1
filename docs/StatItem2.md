# StatItem2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legend** | **List[str]** | A description of the stats data columns | [optional] 
**data** | **List[List[StatItem2DataInnerInner]]** | A list of rows of historical values, as described by the legend | [optional] 

## Example

```python
from layer8_auvik_api_client.models.stat_item2 import StatItem2

# TODO update the JSON string below
json = "{}"
# create an instance of StatItem2 from a JSON string
stat_item2_instance = StatItem2.from_json(json)
# print the JSON string representation of the object
print StatItem2.to_json()

# convert the object into a dict
stat_item2_dict = stat_item2_instance.to_dict()
# create an instance of StatItem2 from a dict
stat_item2_form_dict = stat_item2.from_dict(stat_item2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



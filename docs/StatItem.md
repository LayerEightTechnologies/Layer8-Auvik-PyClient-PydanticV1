# StatItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the statistic | [optional] 
**index** | **str** | Index for multi-part statistics | [optional] 
**legend** | **List[str]** | A description of the stats data columns | [optional] 
**unit** | **List[str]** | Unit type for each stats data column | [optional] 
**data** | **List[List[float]]** | An list of rows of statistics data, as described by the legend | [optional] 

## Example

```python
from layer8_auvik_api_client.models.stat_item import StatItem

# TODO update the JSON string below
json = "{}"
# create an instance of StatItem from a JSON string
stat_item_instance = StatItem.from_json(json)
# print the JSON string representation of the object
print StatItem.to_json()

# convert the object into a dict
stat_item_dict = stat_item_instance.to_dict()
# create an instance of StatItem from a dict
stat_item_form_dict = stat_item.from_dict(stat_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



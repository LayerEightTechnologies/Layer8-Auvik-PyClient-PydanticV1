# AlertRelationshipsEntityDataLinks

Links relating to this entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this interface&#39;s dashboard in the Auvik UI | [optional] 
**var_self** | **str** | Link to this set of network info | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_relationships_entity_data_links import AlertRelationshipsEntityDataLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRelationshipsEntityDataLinks from a JSON string
alert_relationships_entity_data_links_instance = AlertRelationshipsEntityDataLinks.from_json(json)
# print the JSON string representation of the object
print AlertRelationshipsEntityDataLinks.to_json()

# convert the object into a dict
alert_relationships_entity_data_links_dict = alert_relationships_entity_data_links_instance.to_dict()
# create an instance of AlertRelationshipsEntityDataLinks from a dict
alert_relationships_entity_data_links_form_dict = alert_relationships_entity_data_links.from_dict(alert_relationships_entity_data_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



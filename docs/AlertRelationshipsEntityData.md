# AlertRelationshipsEntityData

An entity resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the api | [optional] 
**id** | **str** | The unique identifier for this entity | [optional] 
**links** | [**AlertRelationshipsEntityDataLinks**](AlertRelationshipsEntityDataLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alert_relationships_entity_data import AlertRelationshipsEntityData

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRelationshipsEntityData from a JSON string
alert_relationships_entity_data_instance = AlertRelationshipsEntityData.from_json(json)
# print the JSON string representation of the object
print AlertRelationshipsEntityData.to_json()

# convert the object into a dict
alert_relationships_entity_data_dict = alert_relationships_entity_data_instance.to_dict()
# create an instance of AlertRelationshipsEntityData from a dict
alert_relationships_entity_data_form_dict = alert_relationships_entity_data.from_dict(alert_relationships_entity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



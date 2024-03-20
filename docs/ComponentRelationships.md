# ComponentRelationships

This component's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 
**parent_device** | [**ComponentRelationshipsParentDevice**](ComponentRelationshipsParentDevice.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_relationships import ComponentRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentRelationships from a JSON string
component_relationships_instance = ComponentRelationships.from_json(json)
# print the JSON string representation of the object
print ComponentRelationships.to_json()

# convert the object into a dict
component_relationships_dict = component_relationships_instance.to_dict()
# create an instance of ComponentRelationships from a dict
component_relationships_form_dict = component_relationships.from_dict(component_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



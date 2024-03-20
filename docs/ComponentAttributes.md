# ComponentAttributes

The type-specific properties of the components object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_name** | **str** | This component&#39;s name | 
**component_type** | **str** | This component&#39;s type | 
**current_status** | **str** | High level description of this component&#39;s status | 
**last_modified** | **str** | When one of this component&#39;s attributes was last modified | 

## Example

```python
from layer8_auvik_api_client.models.component_attributes import ComponentAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentAttributes from a JSON string
component_attributes_instance = ComponentAttributes.from_json(json)
# print the JSON string representation of the object
print ComponentAttributes.to_json()

# convert the object into a dict
component_attributes_dict = component_attributes_instance.to_dict()
# create an instance of ComponentAttributes from a dict
component_attributes_form_dict = component_attributes.from_dict(component_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeviceDetailsRelationshipsComponentsAttributes

The type-specific properties of the component object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** |  | 
**configuration_index** | **str** |  | 
**component_name** | **str** | This component&#39;s name | 
**component_type** | **str** | This component&#39;s type | 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_components_attributes import DeviceDetailsRelationshipsComponentsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsComponentsAttributes from a JSON string
device_details_relationships_components_attributes_instance = DeviceDetailsRelationshipsComponentsAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsComponentsAttributes.to_json()

# convert the object into a dict
device_details_relationships_components_attributes_dict = device_details_relationships_components_attributes_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsComponentsAttributes from a dict
device_details_relationships_components_attributes_form_dict = device_details_relationships_components_attributes.from_dict(device_details_relationships_components_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



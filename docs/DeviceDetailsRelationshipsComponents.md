# DeviceDetailsRelationshipsComponents

The components of a device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeviceDetailsRelationshipsComponentsData]**](DeviceDetailsRelationshipsComponentsData.md) | A component resource object | 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_components import DeviceDetailsRelationshipsComponents

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsComponents from a JSON string
device_details_relationships_components_instance = DeviceDetailsRelationshipsComponents.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsComponents.to_json()

# convert the object into a dict
device_details_relationships_components_dict = device_details_relationships_components_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsComponents from a dict
device_details_relationships_components_form_dict = device_details_relationships_components.from_dict(device_details_relationships_components_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



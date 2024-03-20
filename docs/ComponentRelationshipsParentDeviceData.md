# ComponentRelationshipsParentDeviceData

A device resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API. | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**attributes** | [**DeviceLifecycleRelationshipsDeviceDataAttributes**](DeviceLifecycleRelationshipsDeviceDataAttributes.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_relationships_parent_device_data import ComponentRelationshipsParentDeviceData

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentRelationshipsParentDeviceData from a JSON string
component_relationships_parent_device_data_instance = ComponentRelationshipsParentDeviceData.from_json(json)
# print the JSON string representation of the object
print ComponentRelationshipsParentDeviceData.to_json()

# convert the object into a dict
component_relationships_parent_device_data_dict = component_relationships_parent_device_data_instance.to_dict()
# create an instance of ComponentRelationshipsParentDeviceData from a dict
component_relationships_parent_device_data_form_dict = component_relationships_parent_device_data.from_dict(component_relationships_parent_device_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



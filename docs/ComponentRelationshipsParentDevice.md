# ComponentRelationshipsParentDevice

The device associated with this component

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ComponentRelationshipsParentDeviceData**](ComponentRelationshipsParentDeviceData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.component_relationships_parent_device import ComponentRelationshipsParentDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentRelationshipsParentDevice from a JSON string
component_relationships_parent_device_instance = ComponentRelationshipsParentDevice.from_json(json)
# print the JSON string representation of the object
print ComponentRelationshipsParentDevice.to_json()

# convert the object into a dict
component_relationships_parent_device_dict = component_relationships_parent_device_instance.to_dict()
# create an instance of ComponentRelationshipsParentDevice from a dict
component_relationships_parent_device_form_dict = component_relationships_parent_device.from_dict(component_relationships_parent_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



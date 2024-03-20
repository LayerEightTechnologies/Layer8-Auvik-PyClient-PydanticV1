# DeviceDetailsRelationshipsComponentsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for the component associated to the device | [optional] 
**attributes** | [**DeviceDetailsRelationshipsComponentsAttributes**](DeviceDetailsRelationshipsComponentsAttributes.md) |  | [optional] 
**links** | [**DeviceDetailsRelationshipsComponentsLinks**](DeviceDetailsRelationshipsComponentsLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_components_data import DeviceDetailsRelationshipsComponentsData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsComponentsData from a JSON string
device_details_relationships_components_data_instance = DeviceDetailsRelationshipsComponentsData.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsComponentsData.to_json()

# convert the object into a dict
device_details_relationships_components_data_dict = device_details_relationships_components_data_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsComponentsData from a dict
device_details_relationships_components_data_form_dict = device_details_relationships_components_data.from_dict(device_details_relationships_components_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



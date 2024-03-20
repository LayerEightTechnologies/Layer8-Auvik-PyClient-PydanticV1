# DeviceDetailsRelationshipsConfigurationsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for the device associated to the configuration | [optional] 
**attributes** | [**DeviceDetailsRelationshipsConfigurationsAttributes**](DeviceDetailsRelationshipsConfigurationsAttributes.md) |  | [optional] 
**links** | [**DeviceDetailsRelationshipsConfigurationsLinks**](DeviceDetailsRelationshipsConfigurationsLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_configurations_data import DeviceDetailsRelationshipsConfigurationsData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsConfigurationsData from a JSON string
device_details_relationships_configurations_data_instance = DeviceDetailsRelationshipsConfigurationsData.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsConfigurationsData.to_json()

# convert the object into a dict
device_details_relationships_configurations_data_dict = device_details_relationships_configurations_data_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsConfigurationsData from a dict
device_details_relationships_configurations_data_form_dict = device_details_relationships_configurations_data.from_dict(device_details_relationships_configurations_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



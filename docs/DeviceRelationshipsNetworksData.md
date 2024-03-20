# DeviceRelationshipsNetworksData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for this network | [optional] 
**attributes** | [**DeviceRelationshipsNetworksAttributes**](DeviceRelationshipsNetworksAttributes.md) |  | [optional] 
**links** | [**DeviceRelationshipsNetworksLinks**](DeviceRelationshipsNetworksLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_relationships_networks_data import DeviceRelationshipsNetworksData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRelationshipsNetworksData from a JSON string
device_relationships_networks_data_instance = DeviceRelationshipsNetworksData.from_json(json)
# print the JSON string representation of the object
print DeviceRelationshipsNetworksData.to_json()

# convert the object into a dict
device_relationships_networks_data_dict = device_relationships_networks_data_instance.to_dict()
# create an instance of DeviceRelationshipsNetworksData from a dict
device_relationships_networks_data_form_dict = device_relationships_networks_data.from_dict(device_relationships_networks_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



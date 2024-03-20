# NetworkRelationshipsDevicesData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**attributes** | [**NetworkRelationshipsDevicesAttributes**](NetworkRelationshipsDevicesAttributes.md) |  | [optional] 
**links** | [**NetworkRelationshipsDevicesLinks**](NetworkRelationshipsDevicesLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.network_relationships_devices_data import NetworkRelationshipsDevicesData

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRelationshipsDevicesData from a JSON string
network_relationships_devices_data_instance = NetworkRelationshipsDevicesData.from_json(json)
# print the JSON string representation of the object
print NetworkRelationshipsDevicesData.to_json()

# convert the object into a dict
network_relationships_devices_data_dict = network_relationships_devices_data_instance.to_dict()
# create an instance of NetworkRelationshipsDevicesData from a dict
network_relationships_devices_data_form_dict = network_relationships_devices_data.from_dict(network_relationships_devices_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



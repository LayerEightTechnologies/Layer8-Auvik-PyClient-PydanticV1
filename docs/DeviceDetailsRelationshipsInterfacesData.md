# DeviceDetailsRelationshipsInterfacesData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a interface | [optional] 
**attributes** | [**DeviceDetailsRelationshipsInterfacesAttributes**](DeviceDetailsRelationshipsInterfacesAttributes.md) |  | [optional] 
**links** | [**DeviceDetailsRelationshipsInterfacesLinks**](DeviceDetailsRelationshipsInterfacesLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_interfaces_data import DeviceDetailsRelationshipsInterfacesData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsInterfacesData from a JSON string
device_details_relationships_interfaces_data_instance = DeviceDetailsRelationshipsInterfacesData.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsInterfacesData.to_json()

# convert the object into a dict
device_details_relationships_interfaces_data_dict = device_details_relationships_interfaces_data_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsInterfacesData from a dict
device_details_relationships_interfaces_data_form_dict = device_details_relationships_interfaces_data.from_dict(device_details_relationships_interfaces_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



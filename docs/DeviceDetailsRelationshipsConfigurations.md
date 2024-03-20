# DeviceDetailsRelationshipsConfigurations

This device's configurations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeviceDetailsRelationshipsConfigurationsData]**](DeviceDetailsRelationshipsConfigurationsData.md) | A configuration resource object | 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_configurations import DeviceDetailsRelationshipsConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsConfigurations from a JSON string
device_details_relationships_configurations_instance = DeviceDetailsRelationshipsConfigurations.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsConfigurations.to_json()

# convert the object into a dict
device_details_relationships_configurations_dict = device_details_relationships_configurations_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsConfigurations from a dict
device_details_relationships_configurations_form_dict = device_details_relationships_configurations.from_dict(device_details_relationships_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



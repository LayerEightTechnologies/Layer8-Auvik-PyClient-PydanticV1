# DeviceDetailsRelationshipsConfigurationsAttributes

The type-specific properties of the configuration object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_running** | **bool** | Whether the configuration is currently running | 
**backup_time** | **str** | Last backup time of the configuration | 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_configurations_attributes import DeviceDetailsRelationshipsConfigurationsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsConfigurationsAttributes from a JSON string
device_details_relationships_configurations_attributes_instance = DeviceDetailsRelationshipsConfigurationsAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsConfigurationsAttributes.to_json()

# convert the object into a dict
device_details_relationships_configurations_attributes_dict = device_details_relationships_configurations_attributes_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsConfigurationsAttributes from a dict
device_details_relationships_configurations_attributes_form_dict = device_details_relationships_configurations_attributes.from_dict(device_details_relationships_configurations_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



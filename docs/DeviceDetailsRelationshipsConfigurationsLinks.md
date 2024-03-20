# DeviceDetailsRelationshipsConfigurationsLinks

Links relating to this device's configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Link to this configuration | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_configurations_links import DeviceDetailsRelationshipsConfigurationsLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsConfigurationsLinks from a JSON string
device_details_relationships_configurations_links_instance = DeviceDetailsRelationshipsConfigurationsLinks.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsConfigurationsLinks.to_json()

# convert the object into a dict
device_details_relationships_configurations_links_dict = device_details_relationships_configurations_links_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsConfigurationsLinks from a dict
device_details_relationships_configurations_links_form_dict = device_details_relationships_configurations_links.from_dict(device_details_relationships_configurations_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



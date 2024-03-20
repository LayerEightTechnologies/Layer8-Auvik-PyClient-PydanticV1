# DeviceRelationshipsDeviceDetailDataLinks

Links relating to this device details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this device&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this device detail | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_relationships_device_detail_data_links import DeviceRelationshipsDeviceDetailDataLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRelationshipsDeviceDetailDataLinks from a JSON string
device_relationships_device_detail_data_links_instance = DeviceRelationshipsDeviceDetailDataLinks.from_json(json)
# print the JSON string representation of the object
print DeviceRelationshipsDeviceDetailDataLinks.to_json()

# convert the object into a dict
device_relationships_device_detail_data_links_dict = device_relationships_device_detail_data_links_instance.to_dict()
# create an instance of DeviceRelationshipsDeviceDetailDataLinks from a dict
device_relationships_device_detail_data_links_form_dict = device_relationships_device_detail_data_links.from_dict(device_relationships_device_detail_data_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



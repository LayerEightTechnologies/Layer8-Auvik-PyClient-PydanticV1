# DeviceRelationshipsDeviceDetail

Additional attributes and details relating to this device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeviceRelationshipsDeviceDetailData**](DeviceRelationshipsDeviceDetailData.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_relationships_device_detail import DeviceRelationshipsDeviceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRelationshipsDeviceDetail from a JSON string
device_relationships_device_detail_instance = DeviceRelationshipsDeviceDetail.from_json(json)
# print the JSON string representation of the object
print DeviceRelationshipsDeviceDetail.to_json()

# convert the object into a dict
device_relationships_device_detail_dict = device_relationships_device_detail_instance.to_dict()
# create an instance of DeviceRelationshipsDeviceDetail from a dict
device_relationships_device_detail_form_dict = device_relationships_device_detail.from_dict(device_relationships_device_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeviceUsageRelationshipsClientData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Client&#39;s ID | [optional] 
**type** | **str** | The type of this resource object | [optional] 
**attributes** | [**DeviceUsageRelationshipsClientDataAttributes**](DeviceUsageRelationshipsClientDataAttributes.md) |  | [optional] 
**links** | [**ClientUsageResourceObjectLinks**](ClientUsageResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_usage_relationships_client_data import DeviceUsageRelationshipsClientData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageRelationshipsClientData from a JSON string
device_usage_relationships_client_data_instance = DeviceUsageRelationshipsClientData.from_json(json)
# print the JSON string representation of the object
print DeviceUsageRelationshipsClientData.to_json()

# convert the object into a dict
device_usage_relationships_client_data_dict = device_usage_relationships_client_data_instance.to_dict()
# create an instance of DeviceUsageRelationshipsClientData from a dict
device_usage_relationships_client_data_form_dict = device_usage_relationships_client_data.from_dict(device_usage_relationships_client_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeviceUsageResourceObject

Device usage resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Device&#39;s ID | [optional] 
**type** | **str** | The type of this resource object | [optional] 
**attributes** | [**DeviceUsageAttributes**](DeviceUsageAttributes.md) |  | [optional] 
**relationships** | [**DeviceUsageRelationships**](DeviceUsageRelationships.md) |  | [optional] 
**links** | [**DeviceUsageResourceObjectLinks**](DeviceUsageResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_usage_resource_object import DeviceUsageResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageResourceObject from a JSON string
device_usage_resource_object_instance = DeviceUsageResourceObject.from_json(json)
# print the JSON string representation of the object
print DeviceUsageResourceObject.to_json()

# convert the object into a dict
device_usage_resource_object_dict = device_usage_resource_object_instance.to_dict()
# create an instance of DeviceUsageResourceObject from a dict
device_usage_resource_object_form_dict = device_usage_resource_object.from_dict(device_usage_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



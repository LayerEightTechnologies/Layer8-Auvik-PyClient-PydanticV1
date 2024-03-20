# DeviceWarrantyResourceObject

The template for a resource object representing an Auvik device with warranty information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**attributes** | [**DeviceWarrantyAttributes**](DeviceWarrantyAttributes.md) |  | [optional] 
**relationships** | [**DeviceWarrantyRelationships**](DeviceWarrantyRelationships.md) |  | [optional] 
**links** | [**DeviceWarrantyResourceObjectLinks**](DeviceWarrantyResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_warranty_resource_object import DeviceWarrantyResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceWarrantyResourceObject from a JSON string
device_warranty_resource_object_instance = DeviceWarrantyResourceObject.from_json(json)
# print the JSON string representation of the object
print DeviceWarrantyResourceObject.to_json()

# convert the object into a dict
device_warranty_resource_object_dict = device_warranty_resource_object_instance.to_dict()
# create an instance of DeviceWarrantyResourceObject from a dict
device_warranty_resource_object_form_dict = device_warranty_resource_object.from_dict(device_warranty_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



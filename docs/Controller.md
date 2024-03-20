# Controller

Extended details for a controller

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**links** | [**DeviceExtendedDetailsDeviceLinks**](DeviceExtendedDetailsDeviceLinks.md) |  | [optional] 
**attributes** | [**ControllerAllOfAttributes**](ControllerAllOfAttributes.md) |  | [optional] 
**relationships** | [**ControllerAllOfRelationships**](ControllerAllOfRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.controller import Controller

# TODO update the JSON string below
json = "{}"
# create an instance of Controller from a JSON string
controller_instance = Controller.from_json(json)
# print the JSON string representation of the object
print Controller.to_json()

# convert the object into a dict
controller_dict = controller_instance.to_dict()
# create an instance of Controller from a dict
controller_form_dict = controller.from_dict(controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



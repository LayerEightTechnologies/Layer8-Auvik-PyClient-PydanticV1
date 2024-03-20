# Stack

Extended details for a stack

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**links** | [**DeviceExtendedDetailsDeviceLinks**](DeviceExtendedDetailsDeviceLinks.md) |  | [optional] 
**attributes** | [**StackAllOfAttributes**](StackAllOfAttributes.md) |  | [optional] 
**relationships** | [**StackAllOfRelationships**](StackAllOfRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.stack import Stack

# TODO update the JSON string below
json = "{}"
# create an instance of Stack from a JSON string
stack_instance = Stack.from_json(json)
# print the JSON string representation of the object
print Stack.to_json()

# convert the object into a dict
stack_dict = stack_instance.to_dict()
# create an instance of Stack from a dict
stack_form_dict = stack.from_dict(stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



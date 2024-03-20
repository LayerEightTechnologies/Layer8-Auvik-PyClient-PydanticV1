# Hypervisor

Extended details for a hypervisor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**links** | [**DeviceExtendedDetailsDeviceLinks**](DeviceExtendedDetailsDeviceLinks.md) |  | [optional] 
**attributes** | [**HypervisorAllOfAttributes**](HypervisorAllOfAttributes.md) |  | [optional] 
**relationships** | [**DeviceRelationships**](DeviceRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.hypervisor import Hypervisor

# TODO update the JSON string below
json = "{}"
# create an instance of Hypervisor from a JSON string
hypervisor_instance = Hypervisor.from_json(json)
# print the JSON string representation of the object
print Hypervisor.to_json()

# convert the object into a dict
hypervisor_dict = hypervisor_instance.to_dict()
# create an instance of Hypervisor from a dict
hypervisor_form_dict = hypervisor.from_dict(hypervisor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



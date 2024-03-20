# DeviceData

The type-specific properties of the SNMP Poller's Device object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API. | [optional] 
**id** | **str** | The unique identifier for a Device | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_data import DeviceData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceData from a JSON string
device_data_instance = DeviceData.from_json(json)
# print the JSON string representation of the object
print DeviceData.to_json()

# convert the object into a dict
device_data_dict = device_data_instance.to_dict()
# create an instance of DeviceData from a dict
device_data_form_dict = device_data.from_dict(device_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ConfigAttributes

The type-specific properties of the configuration object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_time** | **str** | The time at which this configuration was backed up. | 
**is_running** | **bool** | Whether or not the configuration is currently running on the device. | 

## Example

```python
from layer8_auvik_api_client.models.config_attributes import ConfigAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigAttributes from a JSON string
config_attributes_instance = ConfigAttributes.from_json(json)
# print the JSON string representation of the object
print ConfigAttributes.to_json()

# convert the object into a dict
config_attributes_dict = config_attributes_instance.to_dict()
# create an instance of ConfigAttributes from a dict
config_attributes_form_dict = config_attributes.from_dict(config_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



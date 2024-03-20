# DeviceLifecycleAttributes

The type-specific properties of the devices object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device&#39;s name | 
**sales_availability** | **str** | Availability to order the requested product through Cisco point-of-sale mechanisms | 
**software_maintenance_status** | **str** | Availability of any software maintenance releases or bug fixes to the software product released by Cisco Engineering | 
**security_software_maintenance_status** | **str** | Availability of any planned maintenance release or scheduled software remedy for a security vulnerability issued by Cisco Engineering | 
**last_support_status** | **str** | Availability of service and support for the product | 

## Example

```python
from layer8_auvik_api_client.models.device_lifecycle_attributes import DeviceLifecycleAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLifecycleAttributes from a JSON string
device_lifecycle_attributes_instance = DeviceLifecycleAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceLifecycleAttributes.to_json()

# convert the object into a dict
device_lifecycle_attributes_dict = device_lifecycle_attributes_instance.to_dict()
# create an instance of DeviceLifecycleAttributes from a dict
device_lifecycle_attributes_form_dict = device_lifecycle_attributes.from_dict(device_lifecycle_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



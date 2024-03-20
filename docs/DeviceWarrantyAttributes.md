# DeviceWarrantyAttributes

The type-specific properties of the devices object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device&#39;s name | 
**service_coverage_status** | **str** | Service coverage status | 
**service_attachment_status** | **str** | Service attachment status | [optional] 
**contract_renewal_availability** | **str** | Contract renewal availability | [optional] 
**warranty_coverage_status** | **str** | Warranty coverage status | 
**warranty_expiration_date** | **str** | Warranty expiration date for this device. Value is what is returned by Cisco device, which is not guaranteed to be a date. | 
**recommended_software_version** | **str** | Recommended Devices software version, if known | 

## Example

```python
from layer8_auvik_api_client.models.device_warranty_attributes import DeviceWarrantyAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceWarrantyAttributes from a JSON string
device_warranty_attributes_instance = DeviceWarrantyAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceWarrantyAttributes.to_json()

# convert the object into a dict
device_warranty_attributes_dict = device_warranty_attributes_instance.to_dict()
# create an instance of DeviceWarrantyAttributes from a dict
device_warranty_attributes_form_dict = device_warranty_attributes.from_dict(device_warranty_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



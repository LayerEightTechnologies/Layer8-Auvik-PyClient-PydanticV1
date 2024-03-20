# DeviceDetailsRelationshipsInterfacesAttributes

The type-specific properties of the interfaces object returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_name** | **str** | This interface&#39;s name | 
**mac_address** | **str** | The MAC address of this interface | 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_interfaces_attributes import DeviceDetailsRelationshipsInterfacesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsInterfacesAttributes from a JSON string
device_details_relationships_interfaces_attributes_instance = DeviceDetailsRelationshipsInterfacesAttributes.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsInterfacesAttributes.to_json()

# convert the object into a dict
device_details_relationships_interfaces_attributes_dict = device_details_relationships_interfaces_attributes_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsInterfacesAttributes from a dict
device_details_relationships_interfaces_attributes_form_dict = device_details_relationships_interfaces_attributes.from_dict(device_details_relationships_interfaces_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



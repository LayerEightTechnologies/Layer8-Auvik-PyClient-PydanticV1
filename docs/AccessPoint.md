# AccessPoint

Extended details for an access point

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the API | [optional] 
**id** | **str** | The unique identifier for a device | [optional] 
**links** | [**DeviceExtendedDetailsDeviceLinks**](DeviceExtendedDetailsDeviceLinks.md) |  | [optional] 
**attributes** | [**AccessPointAllOfAttributes**](AccessPointAllOfAttributes.md) |  | [optional] 
**relationships** | [**AccessPointAllOfRelationships**](AccessPointAllOfRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.access_point import AccessPoint

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPoint from a JSON string
access_point_instance = AccessPoint.from_json(json)
# print the JSON string representation of the object
print AccessPoint.to_json()

# convert the object into a dict
access_point_dict = access_point_instance.to_dict()
# create an instance of AccessPoint from a dict
access_point_form_dict = access_point.from_dict(access_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



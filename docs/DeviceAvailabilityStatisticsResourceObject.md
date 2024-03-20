# DeviceAvailabilityStatisticsResourceObject

Device availability statistics resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID for this statistic | [optional] 
**type** | **str** | The type of this resource object | [optional] 
**attributes** | [**StatisticsAttributes**](StatisticsAttributes.md) |  | [optional] 
**relationships** | [**DeviceStatisticsRelationships**](DeviceStatisticsRelationships.md) |  | [optional] 
**links** | [**DeviceStatisticsResourceObjectLinks**](DeviceStatisticsResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_availability_statistics_resource_object import DeviceAvailabilityStatisticsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAvailabilityStatisticsResourceObject from a JSON string
device_availability_statistics_resource_object_instance = DeviceAvailabilityStatisticsResourceObject.from_json(json)
# print the JSON string representation of the object
print DeviceAvailabilityStatisticsResourceObject.to_json()

# convert the object into a dict
device_availability_statistics_resource_object_dict = device_availability_statistics_resource_object_instance.to_dict()
# create an instance of DeviceAvailabilityStatisticsResourceObject from a dict
device_availability_statistics_resource_object_form_dict = device_availability_statistics_resource_object.from_dict(device_availability_statistics_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



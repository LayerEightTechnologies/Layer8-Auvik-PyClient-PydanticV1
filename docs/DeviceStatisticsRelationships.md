# DeviceStatisticsRelationships

Device statistics object's relationships to other resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**DeviceStatisticsRelationshipsDevice**](DeviceStatisticsRelationshipsDevice.md) |  | [optional] 
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_statistics_relationships import DeviceStatisticsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStatisticsRelationships from a JSON string
device_statistics_relationships_instance = DeviceStatisticsRelationships.from_json(json)
# print the JSON string representation of the object
print DeviceStatisticsRelationships.to_json()

# convert the object into a dict
device_statistics_relationships_dict = device_statistics_relationships_instance.to_dict()
# create an instance of DeviceStatisticsRelationships from a dict
device_statistics_relationships_form_dict = device_statistics_relationships.from_dict(device_statistics_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



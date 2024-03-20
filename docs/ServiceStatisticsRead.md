# ServiceStatisticsRead

Root level object per the json-api spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceStatisticsResourceObject**](ServiceStatisticsResourceObject.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.service_statistics_read import ServiceStatisticsRead

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatisticsRead from a JSON string
service_statistics_read_instance = ServiceStatisticsRead.from_json(json)
# print the JSON string representation of the object
print ServiceStatisticsRead.to_json()

# convert the object into a dict
service_statistics_read_dict = service_statistics_read_instance.to_dict()
# create an instance of ServiceStatisticsRead from a dict
service_statistics_read_form_dict = service_statistics_read.from_dict(service_statistics_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



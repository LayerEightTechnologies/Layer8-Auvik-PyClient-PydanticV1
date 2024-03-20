# AlertsResourceObject

The template for a resource object representing an Alert message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object in the api | [optional] 
**id** | **str** | The unique identifier for this alert | [optional] 
**attributes** | [**AlertAttributes**](AlertAttributes.md) |  | [optional] 
**links** | [**AlertsResourceObjectLinks**](AlertsResourceObjectLinks.md) |  | [optional] 
**relationships** | [**AlertRelationships**](AlertRelationships.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.alerts_resource_object import AlertsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsResourceObject from a JSON string
alerts_resource_object_instance = AlertsResourceObject.from_json(json)
# print the JSON string representation of the object
print AlertsResourceObject.to_json()

# convert the object into a dict
alerts_resource_object_dict = alerts_resource_object_instance.to_dict()
# create an instance of AlertsResourceObject from a dict
alerts_resource_object_form_dict = alerts_resource_object.from_dict(alerts_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



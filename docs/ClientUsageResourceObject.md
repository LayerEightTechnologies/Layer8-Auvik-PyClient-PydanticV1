# ClientUsageResourceObject

Client usage resource object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Client tenant&#39;s ID | [optional] 
**type** | **str** | The type of this resource object | [optional] 
**attributes** | [**ClientUsageAttributes**](ClientUsageAttributes.md) |  | [optional] 
**relationships** | [**ClientUsageRelationships**](ClientUsageRelationships.md) |  | [optional] 
**links** | [**ClientUsageResourceObjectLinks**](ClientUsageResourceObjectLinks.md) |  | [optional] 

## Example

```python
from layer8_auvik_api_client.models.client_usage_resource_object import ClientUsageResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUsageResourceObject from a JSON string
client_usage_resource_object_instance = ClientUsageResourceObject.from_json(json)
# print the JSON string representation of the object
print ClientUsageResourceObject.to_json()

# convert the object into a dict
client_usage_resource_object_dict = client_usage_resource_object_instance.to_dict()
# create an instance of ClientUsageResourceObject from a dict
client_usage_resource_object_form_dict = client_usage_resource_object.from_dict(client_usage_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



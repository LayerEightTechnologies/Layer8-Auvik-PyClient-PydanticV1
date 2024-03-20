# DeviceDetailsRelationshipsComponentsLinks

Links relating to this component

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **str** | Link to this component&#39;s dashboard in Auvik | [optional] 
**var_self** | **str** | Link to this component | [optional] 

## Example

```python
from layer8_auvik_api_client.models.device_details_relationships_components_links import DeviceDetailsRelationshipsComponentsLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetailsRelationshipsComponentsLinks from a JSON string
device_details_relationships_components_links_instance = DeviceDetailsRelationshipsComponentsLinks.from_json(json)
# print the JSON string representation of the object
print DeviceDetailsRelationshipsComponentsLinks.to_json()

# convert the object into a dict
device_details_relationships_components_links_dict = device_details_relationships_components_links_instance.to_dict()
# create an instance of DeviceDetailsRelationshipsComponentsLinks from a dict
device_details_relationships_components_links_form_dict = device_details_relationships_components_links.from_dict(device_details_relationships_components_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



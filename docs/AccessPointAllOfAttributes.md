# AccessPointAllOfAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device&#39;s name | 
**last_modified** | **str** | When one of this device&#39;s attributes was last modified | [optional] 
**last_seen_time** | **str** | Last seen online date/time of a device | [optional] 
**device_type** | **str** | What type of device it is | 
**ssid_list** | **List[str]** | List of the AP&#39;s SSIDs | [optional] 

## Example

```python
from layer8_auvik_api_client.models.access_point_all_of_attributes import AccessPointAllOfAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPointAllOfAttributes from a JSON string
access_point_all_of_attributes_instance = AccessPointAllOfAttributes.from_json(json)
# print the JSON string representation of the object
print AccessPointAllOfAttributes.to_json()

# convert the object into a dict
access_point_all_of_attributes_dict = access_point_all_of_attributes_instance.to_dict()
# create an instance of AccessPointAllOfAttributes from a dict
access_point_all_of_attributes_form_dict = access_point_all_of_attributes.from_dict(access_point_all_of_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



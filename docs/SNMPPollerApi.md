# layer8_auvik_api_client.SNMPPollerApi

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_multiple_snmp_poller_setting_devices**](SNMPPollerApi.md#read_multiple_snmp_poller_setting_devices) | **GET** /settings/snmppoller/{snmpPollerSettingId}/devices | Read SNMP Poller Setting&#39;s Devices
[**read_multiple_snmp_poller_settings**](SNMPPollerApi.md#read_multiple_snmp_poller_settings) | **GET** /settings/snmppoller | Read Multiple SNMP Poller Settings
[**read_snmp_poller_setting_single**](SNMPPollerApi.md#read_snmp_poller_setting_single) | **GET** /settings/snmppoller/{snmpPollerSettingId} | Read Single SNMP Poller Setting


# **read_multiple_snmp_poller_setting_devices**
> SnmpPollerSettingDevicesRead read_multiple_snmp_poller_setting_devices(snmp_poller_setting_id, tenants, filter_online_status=filter_online_status, filter_modified_after=filter_modified_after, filter_not_seen_since=filter_not_seen_since, filter_device_type=filter_device_type, filter_make_model=filter_make_model, filter_vendor_name=filter_vendor_name, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read SNMP Poller Setting's Devices

Use Read SNMP Poller Setting's Devices API to pull the list of devices that apply to a specific SNMP Poller Setting Id.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view monitor settings information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_type_schema import DeviceTypeSchema
from layer8_auvik_api_client.models.snmp_poller_setting_devices_read import SnmpPollerSettingDevicesRead
from layer8_auvik_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auvikapi.us1.my.auvik.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = layer8_auvik_api_client.Configuration(
    host = "https://auvikapi.us1.my.auvik.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = layer8_auvik_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with layer8_auvik_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = layer8_auvik_api_client.SNMPPollerApi(api_client)
    snmp_poller_setting_id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | ID of the SNMP Poller Setting that the devices apply to
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from.
    filter_online_status = 'online' # str | Filter by the device’s online status. (optional)
    filter_modified_after = '2018-03-12T12:00:00.000Z' # str | Filter by date and time, only returning entities modified after provided value. (optional)
    filter_not_seen_since = '2018-11-30T18:34:42.652Z' # str | Filter by the last seen online time, returning entities not seen online after the provided value. (optional)
    filter_device_type = layer8_auvik_api_client.DeviceTypeSchema() # DeviceTypeSchema | Filter by device type. (optional)
    filter_make_model = '\"M Series Access Point\"' # str | Filter by the device’s make and model. (optional)
    filter_vendor_name = 'Ubiquiti' # str | Filter by the device’s vendor/manufacturer. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read SNMP Poller Setting's Devices
        api_response = api_instance.read_multiple_snmp_poller_setting_devices(snmp_poller_setting_id, tenants, filter_online_status=filter_online_status, filter_modified_after=filter_modified_after, filter_not_seen_since=filter_not_seen_since, filter_device_type=filter_device_type, filter_make_model=filter_make_model, filter_vendor_name=filter_vendor_name, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of SNMPPollerApi->read_multiple_snmp_poller_setting_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNMPPollerApi->read_multiple_snmp_poller_setting_devices: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_poller_setting_id** | **str**| ID of the SNMP Poller Setting that the devices apply to | 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | 
 **filter_online_status** | **str**| Filter by the device’s online status. | [optional] 
 **filter_modified_after** | **str**| Filter by date and time, only returning entities modified after provided value. | [optional] 
 **filter_not_seen_since** | **str**| Filter by the last seen online time, returning entities not seen online after the provided value. | [optional] 
 **filter_device_type** | [**DeviceTypeSchema**](.md)| Filter by device type. | [optional] 
 **filter_make_model** | **str**| Filter by the device’s make and model. | [optional] 
 **filter_vendor_name** | **str**| Filter by the device’s vendor/manufacturer. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**SnmpPollerSettingDevicesRead**](SnmpPollerSettingDevicesRead.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_multiple_snmp_poller_settings**
> SnmpPollerSettingsRead read_multiple_snmp_poller_settings(tenants, filter_device_id=filter_device_id, filter_use_as=filter_use_as, filter_device_type=filter_device_type, filter_make_model=filter_make_model, filter_vendor_name=filter_vendor_name, filter_oid=filter_oid, filter_name=filter_name, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Multiple SNMP Poller Settings

Use the Read Multiple SNMP Poller Settings API to pull the list of SNMP Poller Settings configured in Auvik.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view monitor settings information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_type_schema import DeviceTypeSchema
from layer8_auvik_api_client.models.snmp_poller_settings_read import SnmpPollerSettingsRead
from layer8_auvik_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auvikapi.us1.my.auvik.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = layer8_auvik_api_client.Configuration(
    host = "https://auvikapi.us1.my.auvik.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = layer8_auvik_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with layer8_auvik_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = layer8_auvik_api_client.SNMPPollerApi(api_client)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from.
    filter_device_id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | Filter by device ID (optional)
    filter_use_as = 'poller' # str | Filter by oid type (optional)
    filter_device_type = layer8_auvik_api_client.DeviceTypeSchema() # DeviceTypeSchema | Filter by device type. (optional)
    filter_make_model = 'M%22Series%20Access%20PointM%22' # str | Filter by the device’s make and model. (optional)
    filter_vendor_name = 'Ubiquiti' # str | Filter by the device’s vendor/manufacturer. (optional)
    filter_oid = '1.3.6.1.2.1.1.3' # str | Filter by OID (optional)
    filter_name = 'M%22SteveM%22' # str | Filter by the name of the SNMP poller setting (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Multiple SNMP Poller Settings
        api_response = api_instance.read_multiple_snmp_poller_settings(tenants, filter_device_id=filter_device_id, filter_use_as=filter_use_as, filter_device_type=filter_device_type, filter_make_model=filter_make_model, filter_vendor_name=filter_vendor_name, filter_oid=filter_oid, filter_name=filter_name, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of SNMPPollerApi->read_multiple_snmp_poller_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNMPPollerApi->read_multiple_snmp_poller_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | 
 **filter_device_id** | **str**| Filter by device ID | [optional] 
 **filter_use_as** | **str**| Filter by oid type | [optional] 
 **filter_device_type** | [**DeviceTypeSchema**](.md)| Filter by device type. | [optional] 
 **filter_make_model** | **str**| Filter by the device’s make and model. | [optional] 
 **filter_vendor_name** | **str**| Filter by the device’s vendor/manufacturer. | [optional] 
 **filter_oid** | **str**| Filter by OID | [optional] 
 **filter_name** | **str**| Filter by the name of the SNMP poller setting | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**SnmpPollerSettingsRead**](SnmpPollerSettingsRead.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_snmp_poller_setting_single**
> SnmpPollerSettingSingleRead read_snmp_poller_setting_single(snmp_poller_setting_id)

Read Single SNMP Poller Setting

Use the Read Single SNMP Poller Setting API to pull details of a specific SNMP Poller Setting configured in Auvik.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view monitor settings information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.snmp_poller_setting_single_read import SnmpPollerSettingSingleRead
from layer8_auvik_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auvikapi.us1.my.auvik.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = layer8_auvik_api_client.Configuration(
    host = "https://auvikapi.us1.my.auvik.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = layer8_auvik_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with layer8_auvik_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = layer8_auvik_api_client.SNMPPollerApi(api_client)
    snmp_poller_setting_id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | ID of the SNMP Poller Setting to retrieve

    try:
        # Read Single SNMP Poller Setting
        api_response = api_instance.read_snmp_poller_setting_single(snmp_poller_setting_id)
        print("The response of SNMPPollerApi->read_snmp_poller_setting_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNMPPollerApi->read_snmp_poller_setting_single: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_poller_setting_id** | **str**| ID of the SNMP Poller Setting to retrieve | 

### Return type

[**SnmpPollerSettingSingleRead**](SnmpPollerSettingSingleRead.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


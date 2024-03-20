# layer8_auvik_api_client.DeviceApi

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_multiple_device_details**](DeviceApi.md#read_multiple_device_details) | **GET** /inventory/device/detail | Read Multiple Devices’ Details
[**read_multiple_device_extended_detail**](DeviceApi.md#read_multiple_device_extended_detail) | **GET** /inventory/device/detail/extended | Read Multiple Devices’ Extended Details
[**read_multiple_device_info**](DeviceApi.md#read_multiple_device_info) | **GET** /inventory/device/info | Read Multiple Devices’ Info
[**read_multiple_device_lifecycle**](DeviceApi.md#read_multiple_device_lifecycle) | **GET** /inventory/device/lifecycle | Read Multiple Devices’ Lifecycle Info
[**read_multiple_device_warranty**](DeviceApi.md#read_multiple_device_warranty) | **GET** /inventory/device/warranty | Read Multiple Devices’ Warranty Info
[**read_single_device_details**](DeviceApi.md#read_single_device_details) | **GET** /inventory/device/detail/{id} | Read a Single Device’s Details
[**read_single_device_extended_detail**](DeviceApi.md#read_single_device_extended_detail) | **GET** /inventory/device/detail/extended/{id} | Read a Single Device’s Extended Details
[**read_single_device_info**](DeviceApi.md#read_single_device_info) | **GET** /inventory/device/info/{id} | Read a Single Device’s Info
[**read_single_device_lifecycle**](DeviceApi.md#read_single_device_lifecycle) | **GET** /inventory/device/lifecycle/{id} | Read a Single Device’s Lifecycle Info
[**read_single_device_warranty**](DeviceApi.md#read_single_device_warranty) | **GET** /inventory/device/warranty/{id} | Read a Single Device’s Warranty Info


# **read_multiple_device_details**
> DeviceDetailsReadMultiple read_multiple_device_details(filter_manage_status=filter_manage_status, filter_discovery_snmp=filter_discovery_snmp, filter_discovery_wmi=filter_discovery_wmi, filter_discovery_login=filter_discovery_login, filter_discovery_v_mware=filter_discovery_v_mware, filter_traffic_insights_status=filter_traffic_insights_status, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Multiple Devices’ Details

Use the Read Multiple Devices’ Details API to pull extra collected information about the various devices Auvik has discovered not already included in the Device Info API. You’ll need the client IDs for the clients you want to run the multiple read against.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device details.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the client(s) whose data you wish to fetch information from. </li>     <li><i>filter[deviceType]=router</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable parameters.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_details_read_multiple import DeviceDetailsReadMultiple
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
    api_instance = layer8_auvik_api_client.DeviceApi(api_client)
    filter_manage_status = true # bool | Filter by managed status (optional)
    filter_discovery_snmp = 'disabled' # str | Filter by the device’s SNMP discovery status. (optional)
    filter_discovery_wmi = 'disabled' # str | Filter by the device’s WMI discovery status. (optional)
    filter_discovery_login = 'disabled' # str | Filter by the device’s Login discovery status. (optional)
    filter_discovery_v_mware = 'disabled' # str | Filter by the device’s VMware discovery status. (optional)
    filter_traffic_insights_status = 'approved' # str | Filter by the device’s TrafficInsights status. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Multiple Devices’ Details
        api_response = api_instance.read_multiple_device_details(filter_manage_status=filter_manage_status, filter_discovery_snmp=filter_discovery_snmp, filter_discovery_wmi=filter_discovery_wmi, filter_discovery_login=filter_discovery_login, filter_discovery_v_mware=filter_discovery_v_mware, filter_traffic_insights_status=filter_traffic_insights_status, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of DeviceApi->read_multiple_device_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_multiple_device_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_manage_status** | **bool**| Filter by managed status | [optional] 
 **filter_discovery_snmp** | **str**| Filter by the device’s SNMP discovery status. | [optional] 
 **filter_discovery_wmi** | **str**| Filter by the device’s WMI discovery status. | [optional] 
 **filter_discovery_login** | **str**| Filter by the device’s Login discovery status. | [optional] 
 **filter_discovery_v_mware** | **str**| Filter by the device’s VMware discovery status. | [optional] 
 **filter_traffic_insights_status** | **str**| Filter by the device’s TrafficInsights status. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**DeviceDetailsReadMultiple**](DeviceDetailsReadMultiple.md)

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

# **read_multiple_device_extended_detail**
> DeviceDetailsExtendedReadMultiple read_multiple_device_extended_detail(filter_device_type, filter_modified_after=filter_modified_after, filter_not_seen_since=filter_not_seen_since, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Multiple Devices’ Extended Details

Use the Read Multiple Devices’ Extended Details API to get many devices’ extended details. Many device types have information collected and tracked by Auvik that are unique to that device type. Use this endpoint to access such information for a given device. You’ll need the client IDs for the clients you want to run the multiple read against.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device extended details.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the client(s) whose data you wish to fetch information from. </li>     <li><i>filter[deviceType]=switch</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable parameters.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_details_extended_read_multiple import DeviceDetailsExtendedReadMultiple
from layer8_auvik_api_client.models.device_type_schema import DeviceTypeSchema
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
    api_instance = layer8_auvik_api_client.DeviceApi(api_client)
    filter_device_type = layer8_auvik_api_client.DeviceTypeSchema() # DeviceTypeSchema | Filter by device type.
    filter_modified_after = '2018-03-12T12:00:00.000Z' # str | Filter by date and time, only returning entities modified after provided value. (optional)
    filter_not_seen_since = '2018-11-30T18:34:42.652Z' # str | Filter by the last seen online time, returning entities not seen online after the provided value. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Multiple Devices’ Extended Details
        api_response = api_instance.read_multiple_device_extended_detail(filter_device_type, filter_modified_after=filter_modified_after, filter_not_seen_since=filter_not_seen_since, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of DeviceApi->read_multiple_device_extended_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_multiple_device_extended_detail: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_device_type** | [**DeviceTypeSchema**](.md)| Filter by device type. | 
 **filter_modified_after** | **str**| Filter by date and time, only returning entities modified after provided value. | [optional] 
 **filter_not_seen_since** | **str**| Filter by the last seen online time, returning entities not seen online after the provided value. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**DeviceDetailsExtendedReadMultiple**](DeviceDetailsExtendedReadMultiple.md)

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

# **read_multiple_device_info**
> DeviceInfoReadMultiple read_multiple_device_info(filter_networks=filter_networks, filter_device_type=filter_device_type, filter_make_model=filter_make_model, filter_vendor_name=filter_vendor_name, filter_online_status=filter_online_status, filter_modified_after=filter_modified_after, filter_not_seen_since=filter_not_seen_since, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before, include=include, fields_device_detail=fields_device_detail)

Read Multiple Devices’ Info

Use the Read Multiple Devices’ Info API to pull the collected information about the various devices Auvik has discovered. You’ll need the client IDs for the clients you want to run the multiple read against.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the client(s) whose data you wish to fetch information from. </li>     <li><i>filter[deviceType]=router</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable parameters.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_info_read_multiple import DeviceInfoReadMultiple
from layer8_auvik_api_client.models.device_type_schema import DeviceTypeSchema
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
    api_instance = layer8_auvik_api_client.DeviceApi(api_client)
    filter_networks = 'MTk5NTAyNzg2ODc3MDYzMTY5LDE5OTUwMjc5MTExMjc4NTkyMw' # str | Filter by IDs of networks this device is on. (optional)
    filter_device_type = layer8_auvik_api_client.DeviceTypeSchema() # DeviceTypeSchema | Filter by device type. (optional)
    filter_make_model = '\"M Series Access Point\"' # str | Filter by the device’s make and model. (optional)
    filter_vendor_name = 'Ubiquiti' # str | Filter by the device’s vendor/manufacturer. (optional)
    filter_online_status = 'online' # str | Filter by the device’s online status. (optional)
    filter_modified_after = '2018-03-12T12:00:00.000Z' # str | Filter by date and time, only returning entities modified after provided value. (optional)
    filter_not_seen_since = '2018-11-30T18:34:42.652Z' # str | Filter by the last seen online time, returning entities not seen online after the provided value. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)
    include = 'deviceDetail' # str | Use to include the full resource objects of the list device relationships. (optional)
    fields_device_detail = 'discoveryStatus,components' # str | Use to limit the attributes that will be returned in the included detail object to only what is specified by this query parameter. Requires <code>include=deviceDetail</code> (optional)

    try:
        # Read Multiple Devices’ Info
        api_response = api_instance.read_multiple_device_info(filter_networks=filter_networks, filter_device_type=filter_device_type, filter_make_model=filter_make_model, filter_vendor_name=filter_vendor_name, filter_online_status=filter_online_status, filter_modified_after=filter_modified_after, filter_not_seen_since=filter_not_seen_since, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before, include=include, fields_device_detail=fields_device_detail)
        print("The response of DeviceApi->read_multiple_device_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_multiple_device_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_networks** | **str**| Filter by IDs of networks this device is on. | [optional] 
 **filter_device_type** | [**DeviceTypeSchema**](.md)| Filter by device type. | [optional] 
 **filter_make_model** | **str**| Filter by the device’s make and model. | [optional] 
 **filter_vendor_name** | **str**| Filter by the device’s vendor/manufacturer. | [optional] 
 **filter_online_status** | **str**| Filter by the device’s online status. | [optional] 
 **filter_modified_after** | **str**| Filter by date and time, only returning entities modified after provided value. | [optional] 
 **filter_not_seen_since** | **str**| Filter by the last seen online time, returning entities not seen online after the provided value. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 
 **include** | **str**| Use to include the full resource objects of the list device relationships. | [optional] 
 **fields_device_detail** | **str**| Use to limit the attributes that will be returned in the included detail object to only what is specified by this query parameter. Requires &lt;code&gt;include&#x3D;deviceDetail&lt;/code&gt; | [optional] 

### Return type

[**DeviceInfoReadMultiple**](DeviceInfoReadMultiple.md)

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

# **read_multiple_device_lifecycle**
> DeviceLifecycleReadMultiple read_multiple_device_lifecycle(filter_sales_availability=filter_sales_availability, filter_software_maintenance_status=filter_software_maintenance_status, filter_security_software_maintenance_status=filter_security_software_maintenance_status, filter_last_support_status=filter_last_support_status, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Multiple Devices’ Lifecycle Info

Use the Read Multiple Devices’ Lifecycle API to pull the collected lifecycle information about the various devices Auvik has discovered. You’ll need the client IDs for the clients you want to run the multiple read against.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the client(s) whose data you wish to fetch information from. </li>     <li><i>filter[salesAvailability]=available</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable parameters.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_lifecycle_read_multiple import DeviceLifecycleReadMultiple
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
    api_instance = layer8_auvik_api_client.DeviceApi(api_client)
    filter_sales_availability = 'available' # str | Filter by sales availability. (optional)
    filter_software_maintenance_status = 'available' # str | Filter by software maintenance status. (optional)
    filter_security_software_maintenance_status = 'available' # str | Filter by security software maintenance status. (optional)
    filter_last_support_status = 'available' # str | Filter by last support status. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Multiple Devices’ Lifecycle Info
        api_response = api_instance.read_multiple_device_lifecycle(filter_sales_availability=filter_sales_availability, filter_software_maintenance_status=filter_software_maintenance_status, filter_security_software_maintenance_status=filter_security_software_maintenance_status, filter_last_support_status=filter_last_support_status, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of DeviceApi->read_multiple_device_lifecycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_multiple_device_lifecycle: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_sales_availability** | **str**| Filter by sales availability. | [optional] 
 **filter_software_maintenance_status** | **str**| Filter by software maintenance status. | [optional] 
 **filter_security_software_maintenance_status** | **str**| Filter by security software maintenance status. | [optional] 
 **filter_last_support_status** | **str**| Filter by last support status. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**DeviceLifecycleReadMultiple**](DeviceLifecycleReadMultiple.md)

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

# **read_multiple_device_warranty**
> DeviceWarrantyReadMultiple read_multiple_device_warranty(filter_covered_under_warranty=filter_covered_under_warranty, filter_covered_under_service=filter_covered_under_service, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Multiple Devices’ Warranty Info

Use the Read Multiple Devices’ Warranty API to pull the collected warranty information about the various devices Auvik has discovered. You’ll need the client IDs for the clients you want to run the multiple read against.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the client(s) whose data you wish to fetch information from. </li>     <li><i>filter[coveredUnderWarranty]=true</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable parameters.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_warranty_read_multiple import DeviceWarrantyReadMultiple
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
    api_instance = layer8_auvik_api_client.DeviceApi(api_client)
    filter_covered_under_warranty = true # bool | Filter by warranty coverage status. (optional)
    filter_covered_under_service = true # bool | Filter by service coverage status. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Multiple Devices’ Warranty Info
        api_response = api_instance.read_multiple_device_warranty(filter_covered_under_warranty=filter_covered_under_warranty, filter_covered_under_service=filter_covered_under_service, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of DeviceApi->read_multiple_device_warranty:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_multiple_device_warranty: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_covered_under_warranty** | **bool**| Filter by warranty coverage status. | [optional] 
 **filter_covered_under_service** | **bool**| Filter by service coverage status. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**DeviceWarrantyReadMultiple**](DeviceWarrantyReadMultiple.md)

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

# **read_single_device_details**
> DeviceDetailsReadSingle read_single_device_details(id)

Read a Single Device’s Details

Use the Read Single Device’s Details API to pull extra collected information about a specific device Auvik has discovered not already included in the Device Info API. You’ll need the device ID for the specific device.<br> <br> To find the device IDs, run the <a href=\"#operation/readMultipleDeviceInfo\">Read Multiple Devices API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device details.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>MTk...2Nw</i> should be the device’s ID.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_details_read_single import DeviceDetailsReadSingle
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
    api_instance = layer8_auvik_api_client.DeviceApi(api_client)
    id = 'id_example' # str | ID of device

    try:
        # Read a Single Device’s Details
        api_response = api_instance.read_single_device_details(id)
        print("The response of DeviceApi->read_single_device_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_single_device_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of device | 

### Return type

[**DeviceDetailsReadSingle**](DeviceDetailsReadSingle.md)

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

# **read_single_device_extended_detail**
> DeviceDetailsExtendedReadSingle read_single_device_extended_detail(id)

Read a Single Device’s Extended Details

Use the Read Single Device’s Extended Details API to get a device’s extended details. Many device types have information collected and tracked by Auvik that are unique to that device type. Use this endpoint to access such information for a given device.<br> <br> To find the device IDs, run the <a href=\"#operation/readMultipleDeviceInfo\">Read Multiple Devices API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device extended details.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>MTk...2Nw</i> should be the device’s ID.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_details_extended_read_single import DeviceDetailsExtendedReadSingle
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
    api_instance = layer8_auvik_api_client.DeviceApi(api_client)
    id = 'id_example' # str | ID of device

    try:
        # Read a Single Device’s Extended Details
        api_response = api_instance.read_single_device_extended_detail(id)
        print("The response of DeviceApi->read_single_device_extended_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_single_device_extended_detail: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of device | 

### Return type

[**DeviceDetailsExtendedReadSingle**](DeviceDetailsExtendedReadSingle.md)

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

# **read_single_device_info**
> DeviceInfoReadSingle read_single_device_info(id, include=include, fields_device_detail=fields_device_detail)

Read a Single Device’s Info

Use the Read Single Device’s Info API to pull the collected information about a specific device Auvik has discovered. You’ll need the device ID for the specific device.<br> <br> To find the device IDs, run the <a href=\"#operation/readMultipleDeviceInfo\">Read Multiple Devices API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>MTk...2Nw</i> should be the device’s ID. </li></ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_info_read_single import DeviceInfoReadSingle
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
    api_instance = layer8_auvik_api_client.DeviceApi(api_client)
    id = 'id_example' # str | ID of device
    include = 'deviceDetail' # str | Use to include the full resource objects of the list device relationships. (optional)
    fields_device_detail = 'discoveryStatus,components' # str | Use to limit the attributes that will be returned in the included detail object to only what is specified by this query parameter. Requires <code>include=deviceDetail</code> (optional)

    try:
        # Read a Single Device’s Info
        api_response = api_instance.read_single_device_info(id, include=include, fields_device_detail=fields_device_detail)
        print("The response of DeviceApi->read_single_device_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_single_device_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of device | 
 **include** | **str**| Use to include the full resource objects of the list device relationships. | [optional] 
 **fields_device_detail** | **str**| Use to limit the attributes that will be returned in the included detail object to only what is specified by this query parameter. Requires &lt;code&gt;include&#x3D;deviceDetail&lt;/code&gt; | [optional] 

### Return type

[**DeviceInfoReadSingle**](DeviceInfoReadSingle.md)

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

# **read_single_device_lifecycle**
> DeviceLifecycleReadSingle read_single_device_lifecycle(id)

Read a Single Device’s Lifecycle Info

Use the Read Single Device’s Lifecycle Info API to pull the collected information about a specific device Auvik has discovered. You’ll need the device ID for the specific device.<br> <br> To find the device IDs, run the <a href=\"#operation/readMultipleDeviceInfo\">Read Multiple Devices API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>MTk...2Nw</i> should be the device’s ID. </li></ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_lifecycle_read_single import DeviceLifecycleReadSingle
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
    api_instance = layer8_auvik_api_client.DeviceApi(api_client)
    id = 'id_example' # str | ID of device

    try:
        # Read a Single Device’s Lifecycle Info
        api_response = api_instance.read_single_device_lifecycle(id)
        print("The response of DeviceApi->read_single_device_lifecycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_single_device_lifecycle: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of device | 

### Return type

[**DeviceLifecycleReadSingle**](DeviceLifecycleReadSingle.md)

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

# **read_single_device_warranty**
> DeviceWarrantyReadSingle read_single_device_warranty(id)

Read a Single Device’s Warranty Info

Use the Read Single Device’s Warranty Info API to pull the collected information about a specific device Auvik has discovered. You’ll need the device ID for the specific device.<br> <br> To find the device IDs, run the <a href=\"#operation/readMultipleDeviceInfo\">Read Multiple Devices API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>MTk...2Nw</i> should be the device’s ID. </li></ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_warranty_read_single import DeviceWarrantyReadSingle
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
    api_instance = layer8_auvik_api_client.DeviceApi(api_client)
    id = 'id_example' # str | ID of device

    try:
        # Read a Single Device’s Warranty Info
        api_response = api_instance.read_single_device_warranty(id)
        print("The response of DeviceApi->read_single_device_warranty:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_single_device_warranty: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of device | 

### Return type

[**DeviceWarrantyReadSingle**](DeviceWarrantyReadSingle.md)

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


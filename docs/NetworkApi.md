# layer8_auvik_api_client.NetworkApi

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_multiple_network_details**](NetworkApi.md#read_multiple_network_details) | **GET** /inventory/network/detail | Read Multiple Networks’ Details
[**read_multiple_network_info**](NetworkApi.md#read_multiple_network_info) | **GET** /inventory/network/info | Read Multiple Networks’ Info
[**read_single_network_details**](NetworkApi.md#read_single_network_details) | **GET** /inventory/network/detail/{id} | Read a Single Network’s Details
[**read_single_network_info**](NetworkApi.md#read_single_network_info) | **GET** /inventory/network/info/{id} | Read a Single Network’s Info


# **read_multiple_network_details**
> NetworkDetailsReadMultiple read_multiple_network_details(filter_network_type=filter_network_type, filter_scan_status=filter_scan_status, filter_devices=filter_devices, filter_modified_after=filter_modified_after, filter_scope=filter_scope, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Multiple Networks’ Details

Use the Read Multiple Networks’ Details API to pull extra collected information about the various networks Auvik has discovered not already included in the Network Info API. You’ll need the client IDs for the clients you want to run the multiple read against.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view network details.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the client(s) whose data you wish to fetch information from. </li>     <li><i>filter[networkType]=routed</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable parameters.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.network_details_read_multiple import NetworkDetailsReadMultiple
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
    api_instance = layer8_auvik_api_client.NetworkApi(api_client)
    filter_network_type = 'routed' # str | Filter by network type. (optional)
    filter_scan_status = 'true' # str | Filter by the network’s scan status. (optional)
    filter_devices = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | Filter by IDs of devices on this network. Filter by multiple values by providing a comma delimited list. (optional)
    filter_modified_after = '2018-03-12T12:00:00.000Z' # str | Filter by date and time, only returning entities modified after provided value. (optional)
    filter_scope = 'private' # str | Filter by the network’s scope (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Multiple Networks’ Details
        api_response = api_instance.read_multiple_network_details(filter_network_type=filter_network_type, filter_scan_status=filter_scan_status, filter_devices=filter_devices, filter_modified_after=filter_modified_after, filter_scope=filter_scope, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of NetworkApi->read_multiple_network_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->read_multiple_network_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_network_type** | **str**| Filter by network type. | [optional] 
 **filter_scan_status** | **str**| Filter by the network’s scan status. | [optional] 
 **filter_devices** | **str**| Filter by IDs of devices on this network. Filter by multiple values by providing a comma delimited list. | [optional] 
 **filter_modified_after** | **str**| Filter by date and time, only returning entities modified after provided value. | [optional] 
 **filter_scope** | **str**| Filter by the network’s scope | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**NetworkDetailsReadMultiple**](NetworkDetailsReadMultiple.md)

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

# **read_multiple_network_info**
> NetworkInfoReadMultiple read_multiple_network_info(filter_network_type=filter_network_type, filter_scan_status=filter_scan_status, filter_devices=filter_devices, filter_modified_after=filter_modified_after, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before, include=include, fields_network_detail=fields_network_detail)

Read Multiple Networks’ Info

Use the Read Multiple Networks’ Info API to pull the collected information about the various networks Auvik has discovered. You’ll need the client IDs for the clients you want to run the multiple read against.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view network information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the client(s) whose data you wish to fetch information from. </li>     <li><i>filter[networkType]=routed</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable parameters.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.network_info_read_multiple import NetworkInfoReadMultiple
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
    api_instance = layer8_auvik_api_client.NetworkApi(api_client)
    filter_network_type = 'routed' # str | Filter by network type. (optional)
    filter_scan_status = 'true' # str | Filter by the network’s scan status. (optional)
    filter_devices = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | Filter by IDs of devices on this network. Filter by multiple values by providing a comma delimited list. (optional)
    filter_modified_after = '2018-03-12T12:00:00.000Z' # str | Filter by date and time, only returning entities modified after provided value. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)
    include = 'networkDetail' # str | Use to include the full resource objects of any of the network’s relationships. (optional)
    fields_network_detail = 'scope,excludedIpAddresses' # str | Use to limit the attributes that will be returned in the included detail object to only what is specified by this query parameter. Requires <code>include=networkDetail</code> (optional)

    try:
        # Read Multiple Networks’ Info
        api_response = api_instance.read_multiple_network_info(filter_network_type=filter_network_type, filter_scan_status=filter_scan_status, filter_devices=filter_devices, filter_modified_after=filter_modified_after, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before, include=include, fields_network_detail=fields_network_detail)
        print("The response of NetworkApi->read_multiple_network_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->read_multiple_network_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_network_type** | **str**| Filter by network type. | [optional] 
 **filter_scan_status** | **str**| Filter by the network’s scan status. | [optional] 
 **filter_devices** | **str**| Filter by IDs of devices on this network. Filter by multiple values by providing a comma delimited list. | [optional] 
 **filter_modified_after** | **str**| Filter by date and time, only returning entities modified after provided value. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 
 **include** | **str**| Use to include the full resource objects of any of the network’s relationships. | [optional] 
 **fields_network_detail** | **str**| Use to limit the attributes that will be returned in the included detail object to only what is specified by this query parameter. Requires &lt;code&gt;include&#x3D;networkDetail&lt;/code&gt; | [optional] 

### Return type

[**NetworkInfoReadMultiple**](NetworkInfoReadMultiple.md)

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

# **read_single_network_details**
> NetworkDetailsReadSingle read_single_network_details(id)

Read a Single Network’s Details

Use the Read Single Networks’s Details API to pull extra collected information about a specific network Auvik has discovered not already included in the network Info API. You’ll need the network ID for the specific network.<br> <br> To find the network IDs, run the <a href=\"#operations/readMultipleNetworkInfo\">Read Multiple Networks API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view network details.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>MTk...yMw</i> should be the network’s ID.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.network_details_read_single import NetworkDetailsReadSingle
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
    api_instance = layer8_auvik_api_client.NetworkApi(api_client)
    id = 'id_example' # str | ID of network

    try:
        # Read a Single Network’s Details
        api_response = api_instance.read_single_network_details(id)
        print("The response of NetworkApi->read_single_network_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->read_single_network_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of network | 

### Return type

[**NetworkDetailsReadSingle**](NetworkDetailsReadSingle.md)

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

# **read_single_network_info**
> NetworkInfoReadSingle read_single_network_info(id, include=include, fields_network_detail=fields_network_detail)

Read a Single Network’s Info

Use the Read Single Network’s Info API to pull the collected information about a specific network Auvik has discovered. You’ll need the network ID for the specific network.<br> <br> To find the network IDs, run the <a href=\"#operations/readMultipleNetworkInfo\">Read Multiple Networks’ Info API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view network information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>MTk...yMw</i> should be the network ID.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.network_info_read_single import NetworkInfoReadSingle
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
    api_instance = layer8_auvik_api_client.NetworkApi(api_client)
    id = 'id_example' # str | ID of network
    include = 'networkDetail' # str | Use to include the full resource objects of any of the network’s relationships. (optional)
    fields_network_detail = 'scope,excludedIpAddresses' # str | Use to limit the attributes that will be returned in the included detail object to only what is specified by this query parameter. Requires <code>include=networkDetail</code> (optional)

    try:
        # Read a Single Network’s Info
        api_response = api_instance.read_single_network_info(id, include=include, fields_network_detail=fields_network_detail)
        print("The response of NetworkApi->read_single_network_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->read_single_network_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of network | 
 **include** | **str**| Use to include the full resource objects of any of the network’s relationships. | [optional] 
 **fields_network_detail** | **str**| Use to limit the attributes that will be returned in the included detail object to only what is specified by this query parameter. Requires &lt;code&gt;include&#x3D;networkDetail&lt;/code&gt; | [optional] 

### Return type

[**NetworkInfoReadSingle**](NetworkInfoReadSingle.md)

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


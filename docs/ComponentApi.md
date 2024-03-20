# layer8_auvik_api_client.ComponentApi

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_multiple_component_info**](ComponentApi.md#read_multiple_component_info) | **GET** /inventory/component/info | Read Multiple Components’ Info
[**read_single_component_info**](ComponentApi.md#read_single_component_info) | **GET** /inventory/component/info/{id} | Read a Single Component’s Info


# **read_multiple_component_info**
> ComponentInfoReadMultiple read_multiple_component_info(filter_modified_after=filter_modified_after, filter_device_id=filter_device_id, filter_device_name=filter_device_name, filter_current_status=filter_current_status, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Multiple Components’ Info

Use the Read Multiple Components’ Info API to pull collected information about various device components Auvik has discovered. You’ll need the client IDs for the clients you want to run the multiple read against.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view component information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the client(s) whose data you wish to fetch information from. </li>     <li><i>filter[currentStatus]=degraded</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable parameters.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.component_info_read_multiple import ComponentInfoReadMultiple
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
    api_instance = layer8_auvik_api_client.ComponentApi(api_client)
    filter_modified_after = '2018-03-12T12:00:00.000Z' # str | Filter by date and time, only returning entities modified after provided value. (optional)
    filter_device_id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | Filter by the component’s parent device’s ID. (optional)
    filter_device_name = '\"ESXi-H153.MSC.MGMT\"' # str | Filter by the component’s parent device’s name. (optional)
    filter_current_status = 'ok' # str | Filter by the component’s current status. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Multiple Components’ Info
        api_response = api_instance.read_multiple_component_info(filter_modified_after=filter_modified_after, filter_device_id=filter_device_id, filter_device_name=filter_device_name, filter_current_status=filter_current_status, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of ComponentApi->read_multiple_component_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentApi->read_multiple_component_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_modified_after** | **str**| Filter by date and time, only returning entities modified after provided value. | [optional] 
 **filter_device_id** | **str**| Filter by the component’s parent device’s ID. | [optional] 
 **filter_device_name** | **str**| Filter by the component’s parent device’s name. | [optional] 
 **filter_current_status** | **str**| Filter by the component’s current status. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**ComponentInfoReadMultiple**](ComponentInfoReadMultiple.md)

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

# **read_single_component_info**
> ComponentInfoReadSingle read_single_component_info(id)

Read a Single Component’s Info

Use the Read Single Component’s Info API to pull collected information about a specific device component Auvik has discovered. You’ll need the component ID you want audit detail for.<br> <br> To find the component IDs, run the <a href=\"#operation/readMultipleComponentInfo\">Read Multiple Components’ Info API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view component information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>MTk...yMw</i> should be the component ID.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.component_info_read_single import ComponentInfoReadSingle
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
    api_instance = layer8_auvik_api_client.ComponentApi(api_client)
    id = 'id_example' # str | ID of component

    try:
        # Read a Single Component’s Info
        api_response = api_instance.read_single_component_info(id)
        print("The response of ComponentApi->read_single_component_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComponentApi->read_single_component_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of component | 

### Return type

[**ComponentInfoReadSingle**](ComponentInfoReadSingle.md)

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


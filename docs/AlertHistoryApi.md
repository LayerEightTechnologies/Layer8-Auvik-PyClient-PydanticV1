# layer8_auvik_api_client.AlertHistoryApi

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_multiple_alert_info**](AlertHistoryApi.md#read_multiple_alert_info) | **GET** /alert/history/info | Read Multiple Alerts’ Info
[**read_single_alert_info**](AlertHistoryApi.md#read_single_alert_info) | **GET** /alert/history/info/{id} | Read a Single Alert’s Info


# **read_multiple_alert_info**
> AlertHistoryInfoReadMultiple read_multiple_alert_info(filter_alert_definition_id=filter_alert_definition_id, filter_alert_specification_id=filter_alert_specification_id, filter_severity=filter_severity, filter_status=filter_status, filter_entity_id=filter_entity_id, filter_dismissed=filter_dismissed, filter_dispatched=filter_dispatched, filter_detected_time_after=filter_detected_time_after, filter_detected_time_before=filter_detected_time_before, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Multiple Alerts’ Info

Use the Read Multiple Alerts’ Info API to pull the collected information about the various alerts that Auvik has triggered.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view alert information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the tenant(s) whose data you wish to fetch information from. </li>     <li><i>severity</i> and <i>warning</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable attributes.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.alert_history_info_read_multiple import AlertHistoryInfoReadMultiple
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
    api_instance = layer8_auvik_api_client.AlertHistoryApi(api_client)
    filter_alert_definition_id = 'MTUyOTA0ODIyMzg5ODgwOTMwLDAsMTIzNAo' # str | Filter by alert definition ID. (optional)
    filter_alert_specification_id = '-100' # str | Filter by alert specification ID. Use 'alertDefinitionId' instead (optional)
    filter_severity = 'warning' # str | Filter by alert severity. (optional)
    filter_status = 'created' # str | Filter by the status of the alert. (optional)
    filter_entity_id = 'MTg2OTI2NTY1MDQ3MDExMDc0LDE5Nzc2OTU1ODM1MTAyMTMxOA' # str | Filter by the related entity ID. (optional)
    filter_dismissed = false # bool | Filter by the dismissed status. (optional)
    filter_dispatched = false # bool | Filter by dispatched status. (optional)
    filter_detected_time_after = 2018-11-21T20:56:38.922Z # bool | Filter by the time which is greater than the given timestamp. (optional)
    filter_detected_time_before = 2018-11-30T18:34:42.652Z # bool | Filter by the time which is less than or equal to the given timestamp. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Multiple Alerts’ Info
        api_response = api_instance.read_multiple_alert_info(filter_alert_definition_id=filter_alert_definition_id, filter_alert_specification_id=filter_alert_specification_id, filter_severity=filter_severity, filter_status=filter_status, filter_entity_id=filter_entity_id, filter_dismissed=filter_dismissed, filter_dispatched=filter_dispatched, filter_detected_time_after=filter_detected_time_after, filter_detected_time_before=filter_detected_time_before, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of AlertHistoryApi->read_multiple_alert_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertHistoryApi->read_multiple_alert_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_alert_definition_id** | **str**| Filter by alert definition ID. | [optional] 
 **filter_alert_specification_id** | **str**| Filter by alert specification ID. Use &#39;alertDefinitionId&#39; instead | [optional] 
 **filter_severity** | **str**| Filter by alert severity. | [optional] 
 **filter_status** | **str**| Filter by the status of the alert. | [optional] 
 **filter_entity_id** | **str**| Filter by the related entity ID. | [optional] 
 **filter_dismissed** | **bool**| Filter by the dismissed status. | [optional] 
 **filter_dispatched** | **bool**| Filter by dispatched status. | [optional] 
 **filter_detected_time_after** | **bool**| Filter by the time which is greater than the given timestamp. | [optional] 
 **filter_detected_time_before** | **bool**| Filter by the time which is less than or equal to the given timestamp. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**AlertHistoryInfoReadMultiple**](AlertHistoryInfoReadMultiple.md)

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

# **read_single_alert_info**
> AlertHistoryInfoReadSingle read_single_alert_info(id)

Read a Single Alert’s Info

Use the Read Single Alert’s Info API to pull the collected information about a specific alert that Auvik has triggered.<br> <br> To find the alert IDs, run the <a href=\"#operation/readMultipleAlertInfo\">Read Multiple Alerts API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view alert information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the tenant(s) whose data you wish to fetch information from. </li>     <li><i>MTk...2Nw</i> should be the alert’s ID.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.alert_history_info_read_single import AlertHistoryInfoReadSingle
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
    api_instance = layer8_auvik_api_client.AlertHistoryApi(api_client)
    id = 'id_example' # str | ID of alert

    try:
        # Read a Single Alert’s Info
        api_response = api_instance.read_single_alert_info(id)
        print("The response of AlertHistoryApi->read_single_alert_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertHistoryApi->read_single_alert_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of alert | 

### Return type

[**AlertHistoryInfoReadSingle**](AlertHistoryInfoReadSingle.md)

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


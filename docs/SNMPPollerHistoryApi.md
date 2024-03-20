# layer8_auvik_api_client.SNMPPollerHistoryApi

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_multiple_snmp_poller_setting_int_history**](SNMPPollerHistoryApi.md#read_multiple_snmp_poller_setting_int_history) | **GET** /stat/snmppoller/int | Read Numeric SNMP Poller Setting&#39;s History
[**read_multiple_snmp_poller_setting_string_history**](SNMPPollerHistoryApi.md#read_multiple_snmp_poller_setting_string_history) | **GET** /stat/snmppoller/string | Read String SNMP Poller Setting&#39;s History


# **read_multiple_snmp_poller_setting_int_history**
> SnmpPollerIntHistoryRead read_multiple_snmp_poller_setting_int_history(filter_from_time, filter_interval, tenants, filter_thru_time=filter_thru_time, filter_device_id=filter_device_id, filter_snmp_poller_setting_id=filter_snmp_poller_setting_id, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Numeric SNMP Poller Setting's History

Use the Read SNMP Poller Setting's History API to fetch the list of historical vaules for a SNMP Poller Setting.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view monitor settings information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>  <li><i>2022-03-10 01:00:00</i> should be the date from which you want to query.</li>     <li><i>2022-03-11 01:00:00</i> should be the date to which you want to query.</li>     <li><i>hour</i> should be the reporting interval for the statistics that are returned.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.snmp_poller_int_history_read import SnmpPollerIntHistoryRead
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
    api_instance = layer8_auvik_api_client.SNMPPollerHistoryApi(api_client)
    filter_from_time = '2022-03-10 01:00:00' # str | Timestamp from which you want to query
    filter_interval = 'hour' # str | Statistics reporting interval
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from.
    filter_thru_time = '2022-03-10 09:00:00' # str | Timestamp to which you want to query (defaults to current time) (optional)
    filter_device_id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | Filter by device ID (optional)
    filter_snmp_poller_setting_id = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE,Y3Vyc29yOk16TXpPVE0wT0RRNU1UQTROemN4TlRneExETXpNemt6TkRnME56QXpORFF5TmpFeU5R' # str | Comma delimited list of SNMP poller setting IDs to request info from. Note this is internal snmpPollerSettingId. The user can get the list of IDs for a specific poller using the GET /settings/snmppoller endpoint. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Numeric SNMP Poller Setting's History
        api_response = api_instance.read_multiple_snmp_poller_setting_int_history(filter_from_time, filter_interval, tenants, filter_thru_time=filter_thru_time, filter_device_id=filter_device_id, filter_snmp_poller_setting_id=filter_snmp_poller_setting_id, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of SNMPPollerHistoryApi->read_multiple_snmp_poller_setting_int_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNMPPollerHistoryApi->read_multiple_snmp_poller_setting_int_history: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_from_time** | **str**| Timestamp from which you want to query | 
 **filter_interval** | **str**| Statistics reporting interval | 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | 
 **filter_thru_time** | **str**| Timestamp to which you want to query (defaults to current time) | [optional] 
 **filter_device_id** | **str**| Filter by device ID | [optional] 
 **filter_snmp_poller_setting_id** | **str**| Comma delimited list of SNMP poller setting IDs to request info from. Note this is internal snmpPollerSettingId. The user can get the list of IDs for a specific poller using the GET /settings/snmppoller endpoint. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**SnmpPollerIntHistoryRead**](SnmpPollerIntHistoryRead.md)

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

# **read_multiple_snmp_poller_setting_string_history**
> SnmpPollerStringHistoryRead read_multiple_snmp_poller_setting_string_history(filter_from_time, tenants, filter_thru_time=filter_thru_time, filter_compact=filter_compact, filter_device_id=filter_device_id, filter_snmp_poller_setting_id=filter_snmp_poller_setting_id, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read String SNMP Poller Setting's History

Use the Read SNMP Poller Setting's History API to fetch the list of historical vaules for a SNMP Poller Setting.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view monitor settings information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>  <li><i>2022-03-10 01:00:00</i> should be the date from which you want to query.</li>     <li><i>2022-03-11 01:00:00</i> should be the date to which you want to query.</li>     <li><i>hour</i> should be the reporting interval for the statistics that are returned.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.snmp_poller_string_history_read import SnmpPollerStringHistoryRead
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
    api_instance = layer8_auvik_api_client.SNMPPollerHistoryApi(api_client)
    filter_from_time = '2022-03-10 01:00:00' # str | Timestamp from which you want to query
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from.
    filter_thru_time = '2022-03-10 09:00:00' # str | Timestamp to which you want to query (defaults to current time) (optional)
    filter_compact = true # bool | Whether to show compact view of the results or not. Compact view only shows changes in value. If compact view is false, dateTime range can be a maximum of 24h (optional)
    filter_device_id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | Filter by device ID (optional)
    filter_snmp_poller_setting_id = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE,Y3Vyc29yOk16TXpPVE0wT0RRNU1UQTROemN4TlRneExETXpNemt6TkRnME56QXpORFF5TmpFeU5R' # str | Comma delimited list of SNMP poller setting IDs to request info from. Note this is internal snmpPollerSettingId. The user can get the list of IDs for a specific poller using the GET /settings/snmppoller endpoint. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read String SNMP Poller Setting's History
        api_response = api_instance.read_multiple_snmp_poller_setting_string_history(filter_from_time, tenants, filter_thru_time=filter_thru_time, filter_compact=filter_compact, filter_device_id=filter_device_id, filter_snmp_poller_setting_id=filter_snmp_poller_setting_id, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of SNMPPollerHistoryApi->read_multiple_snmp_poller_setting_string_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNMPPollerHistoryApi->read_multiple_snmp_poller_setting_string_history: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_from_time** | **str**| Timestamp from which you want to query | 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | 
 **filter_thru_time** | **str**| Timestamp to which you want to query (defaults to current time) | [optional] 
 **filter_compact** | **bool**| Whether to show compact view of the results or not. Compact view only shows changes in value. If compact view is false, dateTime range can be a maximum of 24h | [optional] 
 **filter_device_id** | **str**| Filter by device ID | [optional] 
 **filter_snmp_poller_setting_id** | **str**| Comma delimited list of SNMP poller setting IDs to request info from. Note this is internal snmpPollerSettingId. The user can get the list of IDs for a specific poller using the GET /settings/snmppoller endpoint. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**SnmpPollerStringHistoryRead**](SnmpPollerStringHistoryRead.md)

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


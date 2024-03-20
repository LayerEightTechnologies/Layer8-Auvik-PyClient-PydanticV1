# layer8_auvik_api_client.StatisticsApi

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_component_statistics**](StatisticsApi.md#read_component_statistics) | **GET** /stat/component/{componentType}/{statId} | Read Component Statistics
[**read_device_availability_statistics**](StatisticsApi.md#read_device_availability_statistics) | **GET** /stat/deviceAvailability/{statId} | Read Device Availability Statistics
[**read_device_statistics**](StatisticsApi.md#read_device_statistics) | **GET** /stat/device/{statId} | Read Device Statistics
[**read_interface_statistics**](StatisticsApi.md#read_interface_statistics) | **GET** /stat/interface/{statId} | Read Interface Statistics
[**read_oid_statistics**](StatisticsApi.md#read_oid_statistics) | **GET** /stat/oid/{statId} | Read OID Statistics
[**read_service_statistics**](StatisticsApi.md#read_service_statistics) | **GET** /stat/service/{statId} | Read Service Statistics


# **read_component_statistics**
> ComponentStatisticsRead read_component_statistics(component_type, stat_id, filter_from_time, filter_interval, filter_thru_time=filter_thru_time, filter_component_id=filter_component_id, filter_parent_device=filter_parent_device, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Component Statistics

Use the Read Component Statistics API to fetch detailed statistics of a client's (and client's children if a multi-client) components for a given time range.<br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view component statistics information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>2020-03-10T01:00:00.000Z</i> should be the date from which you want to query.</li>     <li><i>2020-03-11T01:00:00.000Z</i> should be the date to which you want to query.</li>     <li><i>hour</i> should be the reporting interval for the statistics that are returned.</li> </ul>Each component type specified in the query path supports reporting statistics as indicated below: <table><tr><th>componentType</th><th>statId</th></tr><tr><td>cpu</td><td><ul><li>capacity</li><li>latency</li><li>readiness</li><li>ready</li><li>swap</li></ul></td></tr><tr><td>cpuCore</td><td><ul><li>idle</li><li>utilization</li></ul></td></tr><tr><td>disk</td><td><ul><li>latency</li><li>queueLatency</li><li>rate</li><li>totalLatency</li></ul></td></tr><tr><td>fan</td><td><ul><li>speed</li></ul></td></tr></tr><td>memory</td><td><ul><li>counters</li><li>swap</li><li>swapRate</li><li>temperature</li></ul></td></tr><tr><td>powerSupply</td><td><ul><li>power</li></ul></td></tr><tr><td>systemBoard</td><td><ul><li>temperature</li></ul></td></tr></table>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.component_statistics_read import ComponentStatisticsRead
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
    api_instance = layer8_auvik_api_client.StatisticsApi(api_client)
    component_type = 'component_type_example' # str | Component type of statistic to return
    stat_id = 'stat_id_example' # str | ID of statistic to return
    filter_from_time = '2020-03-10T01:00:00.000Z' # str | Timestamp from which you want to query
    filter_interval = 'hour' # str | Statistics reporting interval
    filter_thru_time = '2020-03-11T01:00:00.000Z' # str | Timestamp to which you want to query (defaults to current time) (optional)
    filter_component_id = 'MTkwNzAyOTIzMDk3NzA4MDMzLDA4ODI4MDE3MzQwZGViYTQ5OA' # str | Filter by component ID. (optional)
    filter_parent_device = 'MTkwNzAyOTIzMDk3NzA4MDMzLDMwOTIyNTc3MjQ5ODE5MDgyNA' # str | Filter by the entity's parent device ID. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Component Statistics
        api_response = api_instance.read_component_statistics(component_type, stat_id, filter_from_time, filter_interval, filter_thru_time=filter_thru_time, filter_component_id=filter_component_id, filter_parent_device=filter_parent_device, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of StatisticsApi->read_component_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->read_component_statistics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type of statistic to return | 
 **stat_id** | **str**| ID of statistic to return | 
 **filter_from_time** | **str**| Timestamp from which you want to query | 
 **filter_interval** | **str**| Statistics reporting interval | 
 **filter_thru_time** | **str**| Timestamp to which you want to query (defaults to current time) | [optional] 
 **filter_component_id** | **str**| Filter by component ID. | [optional] 
 **filter_parent_device** | **str**| Filter by the entity&#39;s parent device ID. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**ComponentStatisticsRead**](ComponentStatisticsRead.md)

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

# **read_device_availability_statistics**
> DeviceAvailabilityStatisticsRead read_device_availability_statistics(stat_id, filter_from_time, filter_interval, filter_thru_time=filter_thru_time, filter_device_type=filter_device_type, filter_device_id=filter_device_id, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Device Availability Statistics

Use the Read Device Availability Statistics API to fetch detailed availability statistics of a client’s (and client’s children if a multi-client) devices for a given time range.<br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device availability statistics information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>2020-03-10T01:00:00.000Z</i> should be the date from which you want to query.</li>     <li><i>2020-03-11T01:00:00.000Z</i> should be the date to which you want to query.</li>     <li><i>hour</i> should be the reporting interval for the statistics that are returned.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_availability_statistics_read import DeviceAvailabilityStatisticsRead
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
    api_instance = layer8_auvik_api_client.StatisticsApi(api_client)
    stat_id = 'stat_id_example' # str | ID of statistic to return
    filter_from_time = '2020-03-10T01:00:00.000Z' # str | Timestamp from which you want to query
    filter_interval = 'hour' # str | Statistics reporting interval
    filter_thru_time = '2020-03-11T01:00:00.000Z' # str | Timestamp to which you want to query (defaults to current time) (optional)
    filter_device_type = layer8_auvik_api_client.DeviceTypeSchema() # DeviceTypeSchema | Filter by device type. (optional)
    filter_device_id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | Filter by device ID (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Device Availability Statistics
        api_response = api_instance.read_device_availability_statistics(stat_id, filter_from_time, filter_interval, filter_thru_time=filter_thru_time, filter_device_type=filter_device_type, filter_device_id=filter_device_id, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of StatisticsApi->read_device_availability_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->read_device_availability_statistics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **str**| ID of statistic to return | 
 **filter_from_time** | **str**| Timestamp from which you want to query | 
 **filter_interval** | **str**| Statistics reporting interval | 
 **filter_thru_time** | **str**| Timestamp to which you want to query (defaults to current time) | [optional] 
 **filter_device_type** | [**DeviceTypeSchema**](.md)| Filter by device type. | [optional] 
 **filter_device_id** | **str**| Filter by device ID | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**DeviceAvailabilityStatisticsRead**](DeviceAvailabilityStatisticsRead.md)

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

# **read_device_statistics**
> DeviceStatisticsRead read_device_statistics(stat_id, filter_from_time, filter_interval, filter_thru_time=filter_thru_time, filter_device_type=filter_device_type, filter_device_id=filter_device_id, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Device Statistics

Use the Read Device Statistics API to fetch detailed statistics of a client’s (and client’s children if a multi-client) devices for a given time range.<br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device statistics information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>2020-03-10T01:00:00.000Z</i> should be the date from which you want to query.</li>     <li><i>2020-03-11T01:00:00.000Z</i> should be the date to which you want to query.</li>     <li><i>hour</i> should be the reporting interval for the statistics that are returned.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_statistics_read import DeviceStatisticsRead
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
    api_instance = layer8_auvik_api_client.StatisticsApi(api_client)
    stat_id = 'stat_id_example' # str | ID of statistic to return
    filter_from_time = '2020-03-10T01:00:00.000Z' # str | Timestamp from which you want to query
    filter_interval = 'hour' # str | Statistics reporting interval
    filter_thru_time = '2020-03-11T01:00:00.000Z' # str | Timestamp to which you want to query (defaults to current time) (optional)
    filter_device_type = layer8_auvik_api_client.DeviceTypeSchema() # DeviceTypeSchema | Filter by device type. (optional)
    filter_device_id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | Filter by device ID (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Device Statistics
        api_response = api_instance.read_device_statistics(stat_id, filter_from_time, filter_interval, filter_thru_time=filter_thru_time, filter_device_type=filter_device_type, filter_device_id=filter_device_id, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of StatisticsApi->read_device_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->read_device_statistics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **str**| ID of statistic to return | 
 **filter_from_time** | **str**| Timestamp from which you want to query | 
 **filter_interval** | **str**| Statistics reporting interval | 
 **filter_thru_time** | **str**| Timestamp to which you want to query (defaults to current time) | [optional] 
 **filter_device_type** | [**DeviceTypeSchema**](.md)| Filter by device type. | [optional] 
 **filter_device_id** | **str**| Filter by device ID | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**DeviceStatisticsRead**](DeviceStatisticsRead.md)

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

# **read_interface_statistics**
> InterfaceStatisticsRead read_interface_statistics(stat_id, filter_from_time, filter_interval, filter_thru_time=filter_thru_time, filter_interface_type=filter_interface_type, filter_interface_id=filter_interface_id, filter_parent_device=filter_parent_device, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Interface Statistics

Use the Read Interface Statistics API to fetch detailed statistics of a client's (and client's children if a multi-client) interfaces for a given time range.<br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view interface statistics information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>2020-03-10T01:00:00.000Z</i> should be the date from which you want to query.</li>     <li><i>2020-03-11T01:00:00.000Z</i> should be the date to which you want to query.</li>     <li><i>hour</i> should be the reporting interval for the statistics that are returned.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.interface_statistics_read import InterfaceStatisticsRead
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
    api_instance = layer8_auvik_api_client.StatisticsApi(api_client)
    stat_id = 'stat_id_example' # str | ID of statistic to return
    filter_from_time = '2020-03-10T01:00:00.000Z' # str | Timestamp from which you want to query
    filter_interval = 'hour' # str | Statistics reporting interval
    filter_thru_time = '2020-03-11T01:00:00.000Z' # str | Timestamp to which you want to query (defaults to current time) (optional)
    filter_interface_type = 'ethernet' # str | Filter by interface type. (optional)
    filter_interface_id = 'MTkwNzAyOTIzMDk3NzA4MDMzLDA4ODI4MDE3MzQwZGViYTQ5OA' # str | Filter by interface ID. (optional)
    filter_parent_device = 'MTkwNzAyOTIzMDk3NzA4MDMzLDMwOTIyNTc3MjQ5ODE5MDgyNA' # str | Filter by the entity's parent device ID. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Interface Statistics
        api_response = api_instance.read_interface_statistics(stat_id, filter_from_time, filter_interval, filter_thru_time=filter_thru_time, filter_interface_type=filter_interface_type, filter_interface_id=filter_interface_id, filter_parent_device=filter_parent_device, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of StatisticsApi->read_interface_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->read_interface_statistics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **str**| ID of statistic to return | 
 **filter_from_time** | **str**| Timestamp from which you want to query | 
 **filter_interval** | **str**| Statistics reporting interval | 
 **filter_thru_time** | **str**| Timestamp to which you want to query (defaults to current time) | [optional] 
 **filter_interface_type** | **str**| Filter by interface type. | [optional] 
 **filter_interface_id** | **str**| Filter by interface ID. | [optional] 
 **filter_parent_device** | **str**| Filter by the entity&#39;s parent device ID. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**InterfaceStatisticsRead**](InterfaceStatisticsRead.md)

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

# **read_oid_statistics**
> DeviceOidMonitorRead read_oid_statistics(stat_id, filter_device_id=filter_device_id, filter_device_type=filter_device_type, filter_oid=filter_oid, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read OID Statistics

Use the Read OID Statistics API to fetch the last recorded value of a monitored device OID.<br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view device statistics information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_oid_monitor_read import DeviceOidMonitorRead
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
    api_instance = layer8_auvik_api_client.StatisticsApi(api_client)
    stat_id = 'stat_id_example' # str | ID of statistic to return
    filter_device_id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw' # str | Filter by device ID (optional)
    filter_device_type = layer8_auvik_api_client.DeviceTypeSchema() # DeviceTypeSchema | Filter by device type. (optional)
    filter_oid = '1.3.6.1.2.1.1.3' # str | Filter by OID (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read OID Statistics
        api_response = api_instance.read_oid_statistics(stat_id, filter_device_id=filter_device_id, filter_device_type=filter_device_type, filter_oid=filter_oid, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of StatisticsApi->read_oid_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->read_oid_statistics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **str**| ID of statistic to return | 
 **filter_device_id** | **str**| Filter by device ID | [optional] 
 **filter_device_type** | [**DeviceTypeSchema**](.md)| Filter by device type. | [optional] 
 **filter_oid** | **str**| Filter by OID | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**DeviceOidMonitorRead**](DeviceOidMonitorRead.md)

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

# **read_service_statistics**
> ServiceStatisticsRead read_service_statistics(stat_id, filter_from_time, filter_interval, filter_thru_time=filter_thru_time, filter_service_id=filter_service_id, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Service Statistics

Use the Read Service Statistics API to fetch detailed statistics of a client’s (and client’s children if a multi-client) services for a given time range.<br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view service statistics information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>2020-03-10T01:00:00.000Z</i> should be the date from which you want to query.</li>     <li><i>2020-03-11T01:00:00.000Z</i> should be the date to which you want to query.</li>     <li><i>hour</i> should be the reporting interval for the statistics that are returned.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.service_statistics_read import ServiceStatisticsRead
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
    api_instance = layer8_auvik_api_client.StatisticsApi(api_client)
    stat_id = 'stat_id_example' # str | ID of statistic to return
    filter_from_time = '2020-03-10T01:00:00.000Z' # str | Timestamp from which you want to query
    filter_interval = 'hour' # str | Statistics reporting interval
    filter_thru_time = '2020-03-11T01:00:00.000Z' # str | Timestamp to which you want to query (defaults to current time) (optional)
    filter_service_id = 'NzkyMywtMjAwMDAwMCxzdGF0L3NlcnZpY2UvcGluZ1RpbWU6aG91cg' # str | Filter by service ID (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Service Statistics
        api_response = api_instance.read_service_statistics(stat_id, filter_from_time, filter_interval, filter_thru_time=filter_thru_time, filter_service_id=filter_service_id, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of StatisticsApi->read_service_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->read_service_statistics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stat_id** | **str**| ID of statistic to return | 
 **filter_from_time** | **str**| Timestamp from which you want to query | 
 **filter_interval** | **str**| Statistics reporting interval | 
 **filter_thru_time** | **str**| Timestamp to which you want to query (defaults to current time) | [optional] 
 **filter_service_id** | **str**| Filter by service ID | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**ServiceStatisticsRead**](ServiceStatisticsRead.md)

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


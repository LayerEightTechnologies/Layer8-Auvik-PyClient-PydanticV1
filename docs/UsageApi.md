# layer8_auvik_api_client.UsageApi

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_client_usage**](UsageApi.md#read_client_usage) | **GET** /billing/usage/client | Read Client Usage
[**read_device_usage**](UsageApi.md#read_device_usage) | **GET** /billing/usage/device/{id} | Read Device Usage


# **read_client_usage**
> ClientUsageRead read_client_usage(filter_from_date, filter_thru_date, tenants=tenants)

Read Client Usage

Use the Read Client Usage API to pull a summary of a client’s (and client’s children if a multi-client) usage for a given time range.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view billing information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>2019-06-01</i> should be the date from which you want to query.</li>     <li><i>2019-06-30</i> should be the date to which you want to query.</li>     <li><i>199762235015168516</i> should be the IDs of list of IDs of the clients whose data you wish to query.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.client_usage_read import ClientUsageRead
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
    api_instance = layer8_auvik_api_client.UsageApi(api_client)
    filter_from_date = '2019-06-01' # str | Date from which you want to query
    filter_thru_date = '2019-06-30' # str | Date to which you want to query
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)

    try:
        # Read Client Usage
        api_response = api_instance.read_client_usage(filter_from_date, filter_thru_date, tenants=tenants)
        print("The response of UsageApi->read_client_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->read_client_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_from_date** | **str**| Date from which you want to query | 
 **filter_thru_date** | **str**| Date to which you want to query | 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 

### Return type

[**ClientUsageRead**](ClientUsageRead.md)

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

# **read_device_usage**
> DeviceUsageRead read_device_usage(id, filter_from_date, filter_thru_date)

Read Device Usage

Use the Read Device Usage API to pull a summary of a client’s (and client’s children if a multi-client) usage for a given time range.<br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li><i>user@example.com</i> should be the email address of a user with permissions to view billing information.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>2019-06-01</i> should be the date from which you want to query.</li>     <li><i>2019-06-30</i> should be the date to which you want to query.</li>     <li><i>MTk5...g2Nw</i> should be the ID of the device whose usage you want to query.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.device_usage_read import DeviceUsageRead
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
    api_instance = layer8_auvik_api_client.UsageApi(api_client)
    id = 'id_example' # str | ID of device
    filter_from_date = '2019-06-01' # str | Date from which you want to query
    filter_thru_date = '2019-06-30' # str | Date to which you want to query

    try:
        # Read Device Usage
        api_response = api_instance.read_device_usage(id, filter_from_date, filter_thru_date)
        print("The response of UsageApi->read_device_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->read_device_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of device | 
 **filter_from_date** | **str**| Date from which you want to query | 
 **filter_thru_date** | **str**| Date to which you want to query | 

### Return type

[**DeviceUsageRead**](DeviceUsageRead.md)

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


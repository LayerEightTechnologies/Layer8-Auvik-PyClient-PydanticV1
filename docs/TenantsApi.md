# layer8_auvik_api_client.TenantsApi

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_multiple_tenants**](TenantsApi.md#read_multiple_tenants) | **GET** /tenants | Read Multiple Tenants
[**read_multiple_tenants_detail**](TenantsApi.md#read_multiple_tenants_detail) | **GET** /tenants/detail | Read Multiple Tenants Detail
[**read_single_tenants_detail**](TenantsApi.md#read_single_tenants_detail) | **GET** /tenants/detail/{id} | Read Single Tenant Detail


# **read_multiple_tenants**
> UserTenantsReadMultiple read_multiple_tenants()

Read Multiple Tenants

Use the Read Multiple Tenants API to pull access detail about multiple multi-clients and clients associated with your Auvik user account.<br>         <br>         Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command:         <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>           <li><i>user@example.com</i> should be the email address of a user with permissions to view tenant information.</li>           <li><i>apiKey</i> should be the API key that’s been set for the user.</li>           </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.user_tenants_read_multiple import UserTenantsReadMultiple
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
    api_instance = layer8_auvik_api_client.TenantsApi(api_client)

    try:
        # Read Multiple Tenants
        api_response = api_instance.read_multiple_tenants()
        print("The response of TenantsApi->read_multiple_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->read_multiple_tenants: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**UserTenantsReadMultiple**](UserTenantsReadMultiple.md)

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

# **read_multiple_tenants_detail**
> TenantsDetailReadMultiple read_multiple_tenants_detail(tenant_domain_prefix, filter_available_tenants=filter_available_tenants)

Read Multiple Tenants Detail

Use the Read Multiple Tenants API to pull details for multiple multi-clients and clients associated with your main Auvik account.<br>         <br>         Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command:         <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>           <li><i>user@example.com</i> should be the email address of a user with permissions to view tenant information.</li>           <li><i>apiKey</i> should be the API key that’s been set for the user.</li>           <li><i>mspdemo</i> should be the domain prefix of your main Auvik account. To locate your domain prefix, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li></ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.tenants_detail_read_multiple import TenantsDetailReadMultiple
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
    api_instance = layer8_auvik_api_client.TenantsApi(api_client)
    tenant_domain_prefix = 'mspdemo' # str | Domain prefix of your main Auvik account (tenant).
    filter_available_tenants = true # bool | Filter whether or not a tenant is available, i.e. data can be gotten from them via the API. (optional)

    try:
        # Read Multiple Tenants Detail
        api_response = api_instance.read_multiple_tenants_detail(tenant_domain_prefix, filter_available_tenants=filter_available_tenants)
        print("The response of TenantsApi->read_multiple_tenants_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->read_multiple_tenants_detail: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_domain_prefix** | **str**| Domain prefix of your main Auvik account (tenant). | 
 **filter_available_tenants** | **bool**| Filter whether or not a tenant is available, i.e. data can be gotten from them via the API. | [optional] 

### Return type

[**TenantsDetailReadMultiple**](TenantsDetailReadMultiple.md)

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

# **read_single_tenants_detail**
> TenantsDetailReadSingle read_single_tenants_detail(tenant_domain_prefix, id)

Read Single Tenant Detail

Use the Read a Single Tenant API to pull detail about a specific multi-client and client associated with your main Auvik account. You’ll need the tenant ID for the specific multi-client or client you want detail for.<br>         <br>         You can find the tenant ID for the multi-client or client by <a href=\"#operation/readMultipleTenantsDetail\">Read Multiple Tenants Detail</a>.<br>         <br>         Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command:         <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>           <li><i>user@example.com</i> should be the email address of a user with permissions to edit Client Management.</li>           <li><i>apiKey</i> should be the API key that’s been set for the user.</li>           <li><i>322018492519875477</i> should be the tenant ID.</li>           <li><i>mspdemo</i> should be the domain prefix of your main Auvik account. To locate your domain prefix, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>         </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.tenants_detail_read_single import TenantsDetailReadSingle
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
    api_instance = layer8_auvik_api_client.TenantsApi(api_client)
    tenant_domain_prefix = 'mspdemo' # str | Domain prefix of your main Auvik account (tenant).
    id = 'id_example' # str | ID of tenant

    try:
        # Read Single Tenant Detail
        api_response = api_instance.read_single_tenants_detail(tenant_domain_prefix, id)
        print("The response of TenantsApi->read_single_tenants_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->read_single_tenants_detail: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_domain_prefix** | **str**| Domain prefix of your main Auvik account (tenant). | 
 **id** | **str**| ID of tenant | 

### Return type

[**TenantsDetailReadSingle**](TenantsDetailReadSingle.md)

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


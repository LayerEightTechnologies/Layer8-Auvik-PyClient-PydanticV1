# layer8_auvik_api_client.EntityApi

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_multiple_entity_audit**](EntityApi.md#read_multiple_entity_audit) | **GET** /inventory/entity/audit | Read Multiple Entity Audits
[**read_multiple_entity_note**](EntityApi.md#read_multiple_entity_note) | **GET** /inventory/entity/note | Read Multiple Entity Notes
[**read_single_entity_audit**](EntityApi.md#read_single_entity_audit) | **GET** /inventory/entity/audit/{id} | Read a Single Entity Audit
[**read_single_entity_note**](EntityApi.md#read_single_entity_note) | **GET** /inventory/entity/note/{id} | Read a Single Entity Note


# **read_multiple_entity_audit**
> EntityAuditReadMultiple read_multiple_entity_audit(filter_user=filter_user, filter_category=filter_category, filter_status=filter_status, filter_modified_after=filter_modified_after, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Multiple Entity Audits

Use the Read Multiple Entity Audits API pull information about multiple entity audits for you clients. You’ll need the client IDs for the clients you want to run the multiple read against.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view entity audit history.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the client(s) whose data you wish to fetch information from. </li>     <li><i>filter[status]=created</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable parameters.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.entity_audit_read_multiple import EntityAuditReadMultiple
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
    api_instance = layer8_auvik_api_client.EntityApi(api_client)
    filter_user = '\"John Smith\"' # str | Filter by user name associated to the audit. (optional)
    filter_category = 'unknown' # str | Filter by the audit’s category. (optional)
    filter_status = 'created' # str | Filter by the audit’s status. (optional)
    filter_modified_after = '2018-03-12T12:00:00.000Z' # str | Filter by date and time, only returning entities modified after provided value. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Multiple Entity Audits
        api_response = api_instance.read_multiple_entity_audit(filter_user=filter_user, filter_category=filter_category, filter_status=filter_status, filter_modified_after=filter_modified_after, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of EntityApi->read_multiple_entity_audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->read_multiple_entity_audit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_user** | **str**| Filter by user name associated to the audit. | [optional] 
 **filter_category** | **str**| Filter by the audit’s category. | [optional] 
 **filter_status** | **str**| Filter by the audit’s status. | [optional] 
 **filter_modified_after** | **str**| Filter by date and time, only returning entities modified after provided value. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**EntityAuditReadMultiple**](EntityAuditReadMultiple.md)

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

# **read_multiple_entity_note**
> EntityNotesReadMultiple read_multiple_entity_note(filter_entity_id=filter_entity_id, filter_entity_type=filter_entity_type, filter_entity_name=filter_entity_name, filter_last_modified_by=filter_last_modified_by, filter_modified_after=filter_modified_after, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)

Read Multiple Entity Notes

Use the Read Multiple Entity Notes API pull information about multiple entity notes. You’ll need the client IDs for the clients you want to run the multiple read against.<br> <br> To find the client IDs, run the <a href=\"#operation/readMultipleTenants\">Read Multiple Tenants API.</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view entity notes.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>195798545063742726</i> should be the ID or comma delimited IDs of the client(s) whose data you wish to fetch information from. </li>     <li><i>filter[entityType]=device</i> should be whichever key and value pair you want to filter the result set by. See below for a list of filterable parameters.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.entity_notes_read_multiple import EntityNotesReadMultiple
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
    api_instance = layer8_auvik_api_client.EntityApi(api_client)
    filter_entity_id = 'MTk5NTAyNzg2ODc3MDYzMTY5LDE5OTUwMjc5MTExMjc4NTkyMw' # str | Filter by the entity’s ID. (optional)
    filter_entity_type = 'network' # str | Filter by the entity’s type. (optional)
    filter_entity_name = '\"192.168.4.0/24\"' # str | Filter by the entity’s name. (optional)
    filter_last_modified_by = '\"John User\"' # str | Filter by the user the note was last modified by. (optional)
    filter_modified_after = '2018-03-12T12:00:00.000Z' # str | Filter by date and time, only returning entities modified after provided value. (optional)
    tenants = '199762235015168516,199762235015168004' # str | Comma delimited list of tenant IDs to request info from. (optional)
    page_first = 100.0 # float | For paginated responses, the first N elements will be returned. Used in combination with <code>page[after]</code>. (optional) (default to 100.0)
    page_after = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[first]=100' # str | Cursor after which elements will be returned as a page. The page size is provided by <code>page[first]</code>. (optional)
    page_last = 100.0 # float | For paginated responses, the last N services will be returned. Used in combination with <code>page[before]</code>. (optional) (default to 100.0)
    page_before = 'Y3Vyc29yOjE5OTc2MjIzNTAxNTE2ODAwNCwxOTk3NjI0ODM4MzI2MTI2MTE&page[last]=100' # str | Cursor before which elements will be returned as a page. The page size is provided by <code>page[last]</code>. (optional)

    try:
        # Read Multiple Entity Notes
        api_response = api_instance.read_multiple_entity_note(filter_entity_id=filter_entity_id, filter_entity_type=filter_entity_type, filter_entity_name=filter_entity_name, filter_last_modified_by=filter_last_modified_by, filter_modified_after=filter_modified_after, tenants=tenants, page_first=page_first, page_after=page_after, page_last=page_last, page_before=page_before)
        print("The response of EntityApi->read_multiple_entity_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->read_multiple_entity_note: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_entity_id** | **str**| Filter by the entity’s ID. | [optional] 
 **filter_entity_type** | **str**| Filter by the entity’s type. | [optional] 
 **filter_entity_name** | **str**| Filter by the entity’s name. | [optional] 
 **filter_last_modified_by** | **str**| Filter by the user the note was last modified by. | [optional] 
 **filter_modified_after** | **str**| Filter by date and time, only returning entities modified after provided value. | [optional] 
 **tenants** | **str**| Comma delimited list of tenant IDs to request info from. | [optional] 
 **page_first** | **float**| For paginated responses, the first N elements will be returned. Used in combination with &lt;code&gt;page[after]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_after** | **str**| Cursor after which elements will be returned as a page. The page size is provided by &lt;code&gt;page[first]&lt;/code&gt;. | [optional] 
 **page_last** | **float**| For paginated responses, the last N services will be returned. Used in combination with &lt;code&gt;page[before]&lt;/code&gt;. | [optional] [default to 100.0]
 **page_before** | **str**| Cursor before which elements will be returned as a page. The page size is provided by &lt;code&gt;page[last]&lt;/code&gt;. | [optional] 

### Return type

[**EntityNotesReadMultiple**](EntityNotesReadMultiple.md)

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

# **read_single_entity_audit**
> EntityAuditReadSingle read_single_entity_audit(id)

Read a Single Entity Audit

Use the Single Multiple Entity Audit API pull information about a single entity audit. You’ll need the audit entry ID for the specific audit.<br> <br> To find the audit ID, run the <a href=\"#operation/readMultipleEntityAudit\">Read Multiple Entity Audits API</a><br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view entity audit history.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>MTk...yMw</i> should be the audit’s ID.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.entity_audit_read_single import EntityAuditReadSingle
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
    api_instance = layer8_auvik_api_client.EntityApi(api_client)
    id = 'id_example' # str | ID of entity audit

    try:
        # Read a Single Entity Audit
        api_response = api_instance.read_single_entity_audit(id)
        print("The response of EntityApi->read_single_entity_audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->read_single_entity_audit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of entity audit | 

### Return type

[**EntityAuditReadSingle**](EntityAuditReadSingle.md)

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

# **read_single_entity_note**
> EntityNotesReadSingle read_single_entity_note(id)

Read a Single Entity Note

Use the Read Single Entity Note API to pull the information about a specific entity note. You’ll need the entity note ID for the specific entity note.<br> <br> To find the note IDs the <a href=\"#operation/readMultipleEntityNote\">Read Multiple Entity Notes API</a>.<br> <br> Looking at the detail screen on the right, click cURL to see the command that will be used. Click <b>Copy</b> to copy the details of the command to your clipboard. Be sure to edit the following parameters within the command: <ul>     <li>Within the API URL, <b>us1.my</b> (https://auvikapi.us1.my.auvik.com) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser’s address bar.</li>     <li><i>user@example.com</i> should be the email address of a user with permissions to view entity notes.</li>     <li><i>apiKey</i> should be the API key that’s been set for the user.</li>     <li><i>MTk...yMw</i> should be the note ID.</li> </ul>

### Example

* Basic Authentication (ApiKey):
```python
import time
import os
import layer8_auvik_api_client
from layer8_auvik_api_client.models.entity_notes_read_single import EntityNotesReadSingle
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
    api_instance = layer8_auvik_api_client.EntityApi(api_client)
    id = 'id_example' # str | ID of entity note

    try:
        # Read a Single Entity Note
        api_response = api_instance.read_single_entity_note(id)
        print("The response of EntityApi->read_single_entity_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->read_single_entity_note: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of entity note | 

### Return type

[**EntityNotesReadSingle**](EntityNotesReadSingle.md)

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


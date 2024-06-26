# layer8-auvik-api-client
To use the Auvik APIs, you’ll need a <a href=\"https://support.auvik.com/hc/en-us/articles/204309114-#topic_generate\" target=\"_blank\">valid Auvik user and the user’s API key</a>. The user must also have the correct <a href=\" https://support.auvik.com/hc/en-us/articles/115002815966\" target=\"_blank\">role permissions</a>.<br>
    <br>
    Note: The word <i>tenant</i> as it appears in the API descriptions means one of Auvik’s supported tenant types: multi-client or client.<br><br>All date formats are formatted in the format of YYYY-MM-DDTHH:MM:SS.sssZ, as describe in ISO 8061<br><br>To find out more about Auvik’s APIs, <a href=\"https://support.auvik.com/hc/en-us/articles/360017965092\" target=\"_blank\">click here.</a>

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import layer8_auvik_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import layer8_auvik_api_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import layer8_auvik_api_client
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
    api_instance = layer8_auvik_api_client.AlertApi(api_client)
    id = 'id_example' # str | ID of alert

    try:
        # Dismiss an alert
        api_instance.alert_dismiss_single(id)
    except ApiException as e:
        print("Exception when calling AlertApi->alert_dismiss_single: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://auvikapi.us1.my.auvik.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertApi* | [**alert_dismiss_single**](docs/AlertApi.md#alert_dismiss_single) | **POST** /alert/dismiss/{id} | Dismiss an alert
*AlertHistoryApi* | [**read_multiple_alert_info**](docs/AlertHistoryApi.md#read_multiple_alert_info) | **GET** /alert/history/info | Read Multiple Alerts’ Info
*AlertHistoryApi* | [**read_single_alert_info**](docs/AlertHistoryApi.md#read_single_alert_info) | **GET** /alert/history/info/{id} | Read a Single Alert’s Info
*ComponentApi* | [**read_multiple_component_info**](docs/ComponentApi.md#read_multiple_component_info) | **GET** /inventory/component/info | Read Multiple Components’ Info
*ComponentApi* | [**read_single_component_info**](docs/ComponentApi.md#read_single_component_info) | **GET** /inventory/component/info/{id} | Read a Single Component’s Info
*ConfigurationApi* | [**read_multiple_configurations**](docs/ConfigurationApi.md#read_multiple_configurations) | **GET** /inventory/configuration | Read Multiple Device Configurations
*ConfigurationApi* | [**read_single_configuration**](docs/ConfigurationApi.md#read_single_configuration) | **GET** /inventory/configuration/{id} | Read a Single Device Configuration
*CredentialsApi* | [**verify_credentials**](docs/CredentialsApi.md#verify_credentials) | **GET** /authentication/verify | Verify Credentials
*DeviceApi* | [**read_multiple_device_details**](docs/DeviceApi.md#read_multiple_device_details) | **GET** /inventory/device/detail | Read Multiple Devices’ Details
*DeviceApi* | [**read_multiple_device_extended_detail**](docs/DeviceApi.md#read_multiple_device_extended_detail) | **GET** /inventory/device/detail/extended | Read Multiple Devices’ Extended Details
*DeviceApi* | [**read_multiple_device_info**](docs/DeviceApi.md#read_multiple_device_info) | **GET** /inventory/device/info | Read Multiple Devices’ Info
*DeviceApi* | [**read_multiple_device_lifecycle**](docs/DeviceApi.md#read_multiple_device_lifecycle) | **GET** /inventory/device/lifecycle | Read Multiple Devices’ Lifecycle Info
*DeviceApi* | [**read_multiple_device_warranty**](docs/DeviceApi.md#read_multiple_device_warranty) | **GET** /inventory/device/warranty | Read Multiple Devices’ Warranty Info
*DeviceApi* | [**read_single_device_details**](docs/DeviceApi.md#read_single_device_details) | **GET** /inventory/device/detail/{id} | Read a Single Device’s Details
*DeviceApi* | [**read_single_device_extended_detail**](docs/DeviceApi.md#read_single_device_extended_detail) | **GET** /inventory/device/detail/extended/{id} | Read a Single Device’s Extended Details
*DeviceApi* | [**read_single_device_info**](docs/DeviceApi.md#read_single_device_info) | **GET** /inventory/device/info/{id} | Read a Single Device’s Info
*DeviceApi* | [**read_single_device_lifecycle**](docs/DeviceApi.md#read_single_device_lifecycle) | **GET** /inventory/device/lifecycle/{id} | Read a Single Device’s Lifecycle Info
*DeviceApi* | [**read_single_device_warranty**](docs/DeviceApi.md#read_single_device_warranty) | **GET** /inventory/device/warranty/{id} | Read a Single Device’s Warranty Info
*EntityApi* | [**read_multiple_entity_audit**](docs/EntityApi.md#read_multiple_entity_audit) | **GET** /inventory/entity/audit | Read Multiple Entity Audits
*EntityApi* | [**read_multiple_entity_note**](docs/EntityApi.md#read_multiple_entity_note) | **GET** /inventory/entity/note | Read Multiple Entity Notes
*EntityApi* | [**read_single_entity_audit**](docs/EntityApi.md#read_single_entity_audit) | **GET** /inventory/entity/audit/{id} | Read a Single Entity Audit
*EntityApi* | [**read_single_entity_note**](docs/EntityApi.md#read_single_entity_note) | **GET** /inventory/entity/note/{id} | Read a Single Entity Note
*InterfaceApi* | [**read_multiple_interface_info**](docs/InterfaceApi.md#read_multiple_interface_info) | **GET** /inventory/interface/info | Read Multiple Interfaces Info
*InterfaceApi* | [**read_single_interface_info**](docs/InterfaceApi.md#read_single_interface_info) | **GET** /inventory/interface/info/{id} | Read a Single Interfaces Info
*NetworkApi* | [**read_multiple_network_details**](docs/NetworkApi.md#read_multiple_network_details) | **GET** /inventory/network/detail | Read Multiple Networks’ Details
*NetworkApi* | [**read_multiple_network_info**](docs/NetworkApi.md#read_multiple_network_info) | **GET** /inventory/network/info | Read Multiple Networks’ Info
*NetworkApi* | [**read_single_network_details**](docs/NetworkApi.md#read_single_network_details) | **GET** /inventory/network/detail/{id} | Read a Single Network’s Details
*NetworkApi* | [**read_single_network_info**](docs/NetworkApi.md#read_single_network_info) | **GET** /inventory/network/info/{id} | Read a Single Network’s Info
*SNMPPollerApi* | [**read_multiple_snmp_poller_setting_devices**](docs/SNMPPollerApi.md#read_multiple_snmp_poller_setting_devices) | **GET** /settings/snmppoller/{snmpPollerSettingId}/devices | Read SNMP Poller Setting&#39;s Devices
*SNMPPollerApi* | [**read_multiple_snmp_poller_settings**](docs/SNMPPollerApi.md#read_multiple_snmp_poller_settings) | **GET** /settings/snmppoller | Read Multiple SNMP Poller Settings
*SNMPPollerApi* | [**read_snmp_poller_setting_single**](docs/SNMPPollerApi.md#read_snmp_poller_setting_single) | **GET** /settings/snmppoller/{snmpPollerSettingId} | Read Single SNMP Poller Setting
*SNMPPollerHistoryApi* | [**read_multiple_snmp_poller_setting_int_history**](docs/SNMPPollerHistoryApi.md#read_multiple_snmp_poller_setting_int_history) | **GET** /stat/snmppoller/int | Read Numeric SNMP Poller Setting&#39;s History
*SNMPPollerHistoryApi* | [**read_multiple_snmp_poller_setting_string_history**](docs/SNMPPollerHistoryApi.md#read_multiple_snmp_poller_setting_string_history) | **GET** /stat/snmppoller/string | Read String SNMP Poller Setting&#39;s History
*StatisticsApi* | [**read_component_statistics**](docs/StatisticsApi.md#read_component_statistics) | **GET** /stat/component/{componentType}/{statId} | Read Component Statistics
*StatisticsApi* | [**read_device_availability_statistics**](docs/StatisticsApi.md#read_device_availability_statistics) | **GET** /stat/deviceAvailability/{statId} | Read Device Availability Statistics
*StatisticsApi* | [**read_device_statistics**](docs/StatisticsApi.md#read_device_statistics) | **GET** /stat/device/{statId} | Read Device Statistics
*StatisticsApi* | [**read_interface_statistics**](docs/StatisticsApi.md#read_interface_statistics) | **GET** /stat/interface/{statId} | Read Interface Statistics
*StatisticsApi* | [**read_oid_statistics**](docs/StatisticsApi.md#read_oid_statistics) | **GET** /stat/oid/{statId} | Read OID Statistics
*StatisticsApi* | [**read_service_statistics**](docs/StatisticsApi.md#read_service_statistics) | **GET** /stat/service/{statId} | Read Service Statistics
*TenantsApi* | [**read_multiple_tenants**](docs/TenantsApi.md#read_multiple_tenants) | **GET** /tenants | Read Multiple Tenants
*TenantsApi* | [**read_multiple_tenants_detail**](docs/TenantsApi.md#read_multiple_tenants_detail) | **GET** /tenants/detail | Read Multiple Tenants Detail
*TenantsApi* | [**read_single_tenants_detail**](docs/TenantsApi.md#read_single_tenants_detail) | **GET** /tenants/detail/{id} | Read Single Tenant Detail
*UsageApi* | [**read_client_usage**](docs/UsageApi.md#read_client_usage) | **GET** /billing/usage/client | Read Client Usage
*UsageApi* | [**read_device_usage**](docs/UsageApi.md#read_device_usage) | **GET** /billing/usage/device/{id} | Read Device Usage


## Documentation For Models

 - [AccessPoint](docs/AccessPoint.md)
 - [AccessPointAllOfAttributes](docs/AccessPointAllOfAttributes.md)
 - [AccessPointAllOfRelationships](docs/AccessPointAllOfRelationships.md)
 - [AccessPointAllOfRelationshipsAllOfWirelessClientsInner](docs/AccessPointAllOfRelationshipsAllOfWirelessClientsInner.md)
 - [AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes](docs/AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes.md)
 - [AlertAttributes](docs/AlertAttributes.md)
 - [AlertAttributesExternalTicket](docs/AlertAttributesExternalTicket.md)
 - [AlertHistoryInfoReadMultiple](docs/AlertHistoryInfoReadMultiple.md)
 - [AlertHistoryInfoReadMultipleLinks](docs/AlertHistoryInfoReadMultipleLinks.md)
 - [AlertHistoryInfoReadSingle](docs/AlertHistoryInfoReadSingle.md)
 - [AlertRelationships](docs/AlertRelationships.md)
 - [AlertRelationshipsEntity](docs/AlertRelationshipsEntity.md)
 - [AlertRelationshipsEntityData](docs/AlertRelationshipsEntityData.md)
 - [AlertRelationshipsEntityDataLinks](docs/AlertRelationshipsEntityDataLinks.md)
 - [AlertRelationshipsRelatedAlert](docs/AlertRelationshipsRelatedAlert.md)
 - [AlertRelationshipsRelatedAlertData](docs/AlertRelationshipsRelatedAlertData.md)
 - [AlertRelationshipsRelatedAlertDataAttributes](docs/AlertRelationshipsRelatedAlertDataAttributes.md)
 - [AlertRelationshipsRelatedAlertDataLinks](docs/AlertRelationshipsRelatedAlertDataLinks.md)
 - [AlertsResourceObject](docs/AlertsResourceObject.md)
 - [AlertsResourceObjectLinks](docs/AlertsResourceObjectLinks.md)
 - [AuditAttributes](docs/AuditAttributes.md)
 - [AuditRelationships](docs/AuditRelationships.md)
 - [AuditRelationshipsDevice](docs/AuditRelationshipsDevice.md)
 - [AuditRelationshipsDeviceData](docs/AuditRelationshipsDeviceData.md)
 - [AuditRelationshipsDeviceDataAttributes](docs/AuditRelationshipsDeviceDataAttributes.md)
 - [AuditsResourceObject](docs/AuditsResourceObject.md)
 - [AuditsResourceObjectLinks](docs/AuditsResourceObjectLinks.md)
 - [BaseDeviceExtendedDetailsAttributes](docs/BaseDeviceExtendedDetailsAttributes.md)
 - [BasicError](docs/BasicError.md)
 - [ClientUsageAttributes](docs/ClientUsageAttributes.md)
 - [ClientUsageAttributesClientUsage](docs/ClientUsageAttributesClientUsage.md)
 - [ClientUsageAttributesClientUsageAverageDaysByClientType](docs/ClientUsageAttributesClientUsageAverageDaysByClientType.md)
 - [ClientUsageAttributesClientUsageTotalDaysByClientType](docs/ClientUsageAttributesClientUsageTotalDaysByClientType.md)
 - [ClientUsageAttributesDeviceUsage](docs/ClientUsageAttributesDeviceUsage.md)
 - [ClientUsageAttributesDeviceUsageAverageDaysByClientType](docs/ClientUsageAttributesDeviceUsageAverageDaysByClientType.md)
 - [ClientUsageAttributesDeviceUsageTotalDaysByClientType](docs/ClientUsageAttributesDeviceUsageTotalDaysByClientType.md)
 - [ClientUsageAttributesUsagePeriod](docs/ClientUsageAttributesUsagePeriod.md)
 - [ClientUsageRead](docs/ClientUsageRead.md)
 - [ClientUsageRelationships](docs/ClientUsageRelationships.md)
 - [ClientUsageRelationshipsClients](docs/ClientUsageRelationshipsClients.md)
 - [ClientUsageRelationshipsClientsAttributes](docs/ClientUsageRelationshipsClientsAttributes.md)
 - [ClientUsageRelationshipsClientsData](docs/ClientUsageRelationshipsClientsData.md)
 - [ClientUsageRelationshipsClientsLinks](docs/ClientUsageRelationshipsClientsLinks.md)
 - [ClientUsageRelationshipsDevices](docs/ClientUsageRelationshipsDevices.md)
 - [ClientUsageRelationshipsDevicesAttributes](docs/ClientUsageRelationshipsDevicesAttributes.md)
 - [ClientUsageRelationshipsDevicesData](docs/ClientUsageRelationshipsDevicesData.md)
 - [ClientUsageRelationshipsDevicesLinks](docs/ClientUsageRelationshipsDevicesLinks.md)
 - [ClientUsageResourceObject](docs/ClientUsageResourceObject.md)
 - [ClientUsageResourceObjectLinks](docs/ClientUsageResourceObjectLinks.md)
 - [ComponentAttributes](docs/ComponentAttributes.md)
 - [ComponentInfoReadMultiple](docs/ComponentInfoReadMultiple.md)
 - [ComponentInfoReadMultipleLinks](docs/ComponentInfoReadMultipleLinks.md)
 - [ComponentInfoReadSingle](docs/ComponentInfoReadSingle.md)
 - [ComponentRelationships](docs/ComponentRelationships.md)
 - [ComponentRelationshipsParentDevice](docs/ComponentRelationshipsParentDevice.md)
 - [ComponentRelationshipsParentDeviceData](docs/ComponentRelationshipsParentDeviceData.md)
 - [ComponentStatisticsRead](docs/ComponentStatisticsRead.md)
 - [ComponentStatisticsRelationships](docs/ComponentStatisticsRelationships.md)
 - [ComponentStatisticsRelationshipsComponent](docs/ComponentStatisticsRelationshipsComponent.md)
 - [ComponentStatisticsRelationshipsComponentData](docs/ComponentStatisticsRelationshipsComponentData.md)
 - [ComponentStatisticsRelationshipsComponentDataLinks](docs/ComponentStatisticsRelationshipsComponentDataLinks.md)
 - [ComponentStatisticsResourceObject](docs/ComponentStatisticsResourceObject.md)
 - [ComponentStatisticsResourceObjectLinks](docs/ComponentStatisticsResourceObjectLinks.md)
 - [ComponentsResourceObject](docs/ComponentsResourceObject.md)
 - [ComponentsResourceObjectLinks](docs/ComponentsResourceObjectLinks.md)
 - [ConfigAttributes](docs/ConfigAttributes.md)
 - [ConfigReadMultiple](docs/ConfigReadMultiple.md)
 - [ConfigReadMultipleLinks](docs/ConfigReadMultipleLinks.md)
 - [ConfigReadSingle](docs/ConfigReadSingle.md)
 - [ConfigRelationships](docs/ConfigRelationships.md)
 - [ConfigResourceObject](docs/ConfigResourceObject.md)
 - [ConfigResourceObjectLinks](docs/ConfigResourceObjectLinks.md)
 - [Controller](docs/Controller.md)
 - [ControllerAllOfAttributes](docs/ControllerAllOfAttributes.md)
 - [ControllerAllOfRelationships](docs/ControllerAllOfRelationships.md)
 - [ControllerAllOfRelationshipsAllOfAccessPointsInner](docs/ControllerAllOfRelationshipsAllOfAccessPointsInner.md)
 - [ControllerAllOfRelationshipsAllOfAccessPointsInnerAttributes](docs/ControllerAllOfRelationshipsAllOfAccessPointsInnerAttributes.md)
 - [ControllerAllOfRelationshipsAllOfAccessPointsInnerLinks](docs/ControllerAllOfRelationshipsAllOfAccessPointsInnerLinks.md)
 - [Device](docs/Device.md)
 - [DeviceAttributes](docs/DeviceAttributes.md)
 - [DeviceAvailabilityStatisticsRead](docs/DeviceAvailabilityStatisticsRead.md)
 - [DeviceAvailabilityStatisticsResourceObject](docs/DeviceAvailabilityStatisticsResourceObject.md)
 - [DeviceData](docs/DeviceData.md)
 - [DeviceDetailsAttributes](docs/DeviceDetailsAttributes.md)
 - [DeviceDetailsAttributesDiscoveryStatus](docs/DeviceDetailsAttributesDiscoveryStatus.md)
 - [DeviceDetailsExtendedReadMultiple](docs/DeviceDetailsExtendedReadMultiple.md)
 - [DeviceDetailsExtendedReadMultipleLinks](docs/DeviceDetailsExtendedReadMultipleLinks.md)
 - [DeviceDetailsExtendedReadSingle](docs/DeviceDetailsExtendedReadSingle.md)
 - [DeviceDetailsReadMultiple](docs/DeviceDetailsReadMultiple.md)
 - [DeviceDetailsReadMultipleLinks](docs/DeviceDetailsReadMultipleLinks.md)
 - [DeviceDetailsReadSingle](docs/DeviceDetailsReadSingle.md)
 - [DeviceDetailsRelationships](docs/DeviceDetailsRelationships.md)
 - [DeviceDetailsRelationshipsComponents](docs/DeviceDetailsRelationshipsComponents.md)
 - [DeviceDetailsRelationshipsComponentsAttributes](docs/DeviceDetailsRelationshipsComponentsAttributes.md)
 - [DeviceDetailsRelationshipsComponentsData](docs/DeviceDetailsRelationshipsComponentsData.md)
 - [DeviceDetailsRelationshipsComponentsLinks](docs/DeviceDetailsRelationshipsComponentsLinks.md)
 - [DeviceDetailsRelationshipsConfigurations](docs/DeviceDetailsRelationshipsConfigurations.md)
 - [DeviceDetailsRelationshipsConfigurationsAttributes](docs/DeviceDetailsRelationshipsConfigurationsAttributes.md)
 - [DeviceDetailsRelationshipsConfigurationsData](docs/DeviceDetailsRelationshipsConfigurationsData.md)
 - [DeviceDetailsRelationshipsConfigurationsLinks](docs/DeviceDetailsRelationshipsConfigurationsLinks.md)
 - [DeviceDetailsRelationshipsConnectedDevices](docs/DeviceDetailsRelationshipsConnectedDevices.md)
 - [DeviceDetailsRelationshipsConnectedDevicesAttributes](docs/DeviceDetailsRelationshipsConnectedDevicesAttributes.md)
 - [DeviceDetailsRelationshipsConnectedDevicesData](docs/DeviceDetailsRelationshipsConnectedDevicesData.md)
 - [DeviceDetailsRelationshipsConnectedDevicesLinks](docs/DeviceDetailsRelationshipsConnectedDevicesLinks.md)
 - [DeviceDetailsRelationshipsInterfaces](docs/DeviceDetailsRelationshipsInterfaces.md)
 - [DeviceDetailsRelationshipsInterfacesAttributes](docs/DeviceDetailsRelationshipsInterfacesAttributes.md)
 - [DeviceDetailsRelationshipsInterfacesData](docs/DeviceDetailsRelationshipsInterfacesData.md)
 - [DeviceDetailsRelationshipsInterfacesLinks](docs/DeviceDetailsRelationshipsInterfacesLinks.md)
 - [DeviceDetailsResourceObject](docs/DeviceDetailsResourceObject.md)
 - [DeviceDetailsResourceObjectLinks](docs/DeviceDetailsResourceObjectLinks.md)
 - [DeviceExtendedDetailResourceObject](docs/DeviceExtendedDetailResourceObject.md)
 - [DeviceExtendedDetailsDevice](docs/DeviceExtendedDetailsDevice.md)
 - [DeviceExtendedDetailsDeviceLinks](docs/DeviceExtendedDetailsDeviceLinks.md)
 - [DeviceInfoReadMultiple](docs/DeviceInfoReadMultiple.md)
 - [DeviceInfoReadMultipleLinks](docs/DeviceInfoReadMultipleLinks.md)
 - [DeviceInfoReadSingle](docs/DeviceInfoReadSingle.md)
 - [DeviceLifecycleAttributes](docs/DeviceLifecycleAttributes.md)
 - [DeviceLifecycleReadMultiple](docs/DeviceLifecycleReadMultiple.md)
 - [DeviceLifecycleReadMultipleLinks](docs/DeviceLifecycleReadMultipleLinks.md)
 - [DeviceLifecycleReadSingle](docs/DeviceLifecycleReadSingle.md)
 - [DeviceLifecycleRelationships](docs/DeviceLifecycleRelationships.md)
 - [DeviceLifecycleRelationshipsDevice](docs/DeviceLifecycleRelationshipsDevice.md)
 - [DeviceLifecycleRelationshipsDeviceData](docs/DeviceLifecycleRelationshipsDeviceData.md)
 - [DeviceLifecycleRelationshipsDeviceDataAttributes](docs/DeviceLifecycleRelationshipsDeviceDataAttributes.md)
 - [DeviceLifecycleResourceObject](docs/DeviceLifecycleResourceObject.md)
 - [DeviceLifecycleResourceObjectLinks](docs/DeviceLifecycleResourceObjectLinks.md)
 - [DeviceOidMonitorRead](docs/DeviceOidMonitorRead.md)
 - [DeviceOidMonitorReadLinks](docs/DeviceOidMonitorReadLinks.md)
 - [DeviceOidMonitorResourceObject](docs/DeviceOidMonitorResourceObject.md)
 - [DeviceOidMonitorResourceObjectLinks](docs/DeviceOidMonitorResourceObjectLinks.md)
 - [DeviceRelationships](docs/DeviceRelationships.md)
 - [DeviceRelationshipsDeviceDetail](docs/DeviceRelationshipsDeviceDetail.md)
 - [DeviceRelationshipsDeviceDetailData](docs/DeviceRelationshipsDeviceDetailData.md)
 - [DeviceRelationshipsDeviceDetailDataLinks](docs/DeviceRelationshipsDeviceDetailDataLinks.md)
 - [DeviceRelationshipsNetworks](docs/DeviceRelationshipsNetworks.md)
 - [DeviceRelationshipsNetworksAttributes](docs/DeviceRelationshipsNetworksAttributes.md)
 - [DeviceRelationshipsNetworksData](docs/DeviceRelationshipsNetworksData.md)
 - [DeviceRelationshipsNetworksLinks](docs/DeviceRelationshipsNetworksLinks.md)
 - [DeviceStatisticsRead](docs/DeviceStatisticsRead.md)
 - [DeviceStatisticsRelationships](docs/DeviceStatisticsRelationships.md)
 - [DeviceStatisticsRelationshipsDevice](docs/DeviceStatisticsRelationshipsDevice.md)
 - [DeviceStatisticsRelationshipsDeviceData](docs/DeviceStatisticsRelationshipsDeviceData.md)
 - [DeviceStatisticsResourceObject](docs/DeviceStatisticsResourceObject.md)
 - [DeviceStatisticsResourceObjectLinks](docs/DeviceStatisticsResourceObjectLinks.md)
 - [DeviceTypeSchema](docs/DeviceTypeSchema.md)
 - [DeviceUsageAttributes](docs/DeviceUsageAttributes.md)
 - [DeviceUsageAttributesAverageDaysByClientType](docs/DeviceUsageAttributesAverageDaysByClientType.md)
 - [DeviceUsageAttributesTotalDaysByClientType](docs/DeviceUsageAttributesTotalDaysByClientType.md)
 - [DeviceUsageRead](docs/DeviceUsageRead.md)
 - [DeviceUsageRelationships](docs/DeviceUsageRelationships.md)
 - [DeviceUsageRelationshipsClient](docs/DeviceUsageRelationshipsClient.md)
 - [DeviceUsageRelationshipsClientData](docs/DeviceUsageRelationshipsClientData.md)
 - [DeviceUsageRelationshipsClientDataAttributes](docs/DeviceUsageRelationshipsClientDataAttributes.md)
 - [DeviceUsageResourceObject](docs/DeviceUsageResourceObject.md)
 - [DeviceUsageResourceObjectLinks](docs/DeviceUsageResourceObjectLinks.md)
 - [DeviceWarrantyAttributes](docs/DeviceWarrantyAttributes.md)
 - [DeviceWarrantyReadMultiple](docs/DeviceWarrantyReadMultiple.md)
 - [DeviceWarrantyReadMultipleLinks](docs/DeviceWarrantyReadMultipleLinks.md)
 - [DeviceWarrantyReadSingle](docs/DeviceWarrantyReadSingle.md)
 - [DeviceWarrantyRelationships](docs/DeviceWarrantyRelationships.md)
 - [DeviceWarrantyResourceObject](docs/DeviceWarrantyResourceObject.md)
 - [DeviceWarrantyResourceObjectLinks](docs/DeviceWarrantyResourceObjectLinks.md)
 - [DevicesResourceObject](docs/DevicesResourceObject.md)
 - [DevicesResourceObjectLinks](docs/DevicesResourceObjectLinks.md)
 - [EndpointStats](docs/EndpointStats.md)
 - [EntityAuditReadMultiple](docs/EntityAuditReadMultiple.md)
 - [EntityAuditReadMultipleLinks](docs/EntityAuditReadMultipleLinks.md)
 - [EntityAuditReadSingle](docs/EntityAuditReadSingle.md)
 - [EntityNotesReadMultiple](docs/EntityNotesReadMultiple.md)
 - [EntityNotesReadMultipleLinks](docs/EntityNotesReadMultipleLinks.md)
 - [EntityNotesReadSingle](docs/EntityNotesReadSingle.md)
 - [Hypervisor](docs/Hypervisor.md)
 - [HypervisorAllOfAttributes](docs/HypervisorAllOfAttributes.md)
 - [HypervisorAllOfAttributesAllOfVirtualMachinesInner](docs/HypervisorAllOfAttributesAllOfVirtualMachinesInner.md)
 - [HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner](docs/HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner.md)
 - [InterfaceAttributes](docs/InterfaceAttributes.md)
 - [InterfaceInfoReadMultiple](docs/InterfaceInfoReadMultiple.md)
 - [InterfaceInfoReadMultipleLinks](docs/InterfaceInfoReadMultipleLinks.md)
 - [InterfaceInfoReadSingle](docs/InterfaceInfoReadSingle.md)
 - [InterfaceRelationships](docs/InterfaceRelationships.md)
 - [InterfaceRelationshipsConnectedTo](docs/InterfaceRelationshipsConnectedTo.md)
 - [InterfaceRelationshipsConnectedToData](docs/InterfaceRelationshipsConnectedToData.md)
 - [InterfaceRelationshipsConnectedToLinks](docs/InterfaceRelationshipsConnectedToLinks.md)
 - [InterfaceRelationshipsNetworks](docs/InterfaceRelationshipsNetworks.md)
 - [InterfaceRelationshipsNetworksData](docs/InterfaceRelationshipsNetworksData.md)
 - [InterfaceRelationshipsNetworksLinks](docs/InterfaceRelationshipsNetworksLinks.md)
 - [InterfaceRelationshipsParentDevice](docs/InterfaceRelationshipsParentDevice.md)
 - [InterfaceRelationshipsParentDeviceData](docs/InterfaceRelationshipsParentDeviceData.md)
 - [InterfaceRelationshipsParentDeviceDataLinks](docs/InterfaceRelationshipsParentDeviceDataLinks.md)
 - [InterfaceResourceObject](docs/InterfaceResourceObject.md)
 - [InterfaceResourceObjectLinks](docs/InterfaceResourceObjectLinks.md)
 - [InterfaceStatisticsRead](docs/InterfaceStatisticsRead.md)
 - [InterfaceStatisticsRelationships](docs/InterfaceStatisticsRelationships.md)
 - [InterfaceStatisticsRelationshipsInterface](docs/InterfaceStatisticsRelationshipsInterface.md)
 - [InterfaceStatisticsRelationshipsInterfaceData](docs/InterfaceStatisticsRelationshipsInterfaceData.md)
 - [InterfaceStatisticsRelationshipsInterfaceDataLinks](docs/InterfaceStatisticsRelationshipsInterfaceDataLinks.md)
 - [InterfaceStatisticsResourceObject](docs/InterfaceStatisticsResourceObject.md)
 - [InterfaceStatisticsResourceObjectLinks](docs/InterfaceStatisticsResourceObjectLinks.md)
 - [Meta](docs/Meta.md)
 - [MiscDevice](docs/MiscDevice.md)
 - [MiscDeviceAllOfAttributes](docs/MiscDeviceAllOfAttributes.md)
 - [MiscDeviceAllOfAttributesAllOfTunnelsInner](docs/MiscDeviceAllOfAttributesAllOfTunnelsInner.md)
 - [NetworkAttributes](docs/NetworkAttributes.md)
 - [NetworkDetailsAttributes](docs/NetworkDetailsAttributes.md)
 - [NetworkDetailsReadMultiple](docs/NetworkDetailsReadMultiple.md)
 - [NetworkDetailsReadMultipleLinks](docs/NetworkDetailsReadMultipleLinks.md)
 - [NetworkDetailsReadSingle](docs/NetworkDetailsReadSingle.md)
 - [NetworkDetailsRelationships](docs/NetworkDetailsRelationships.md)
 - [NetworkDetailsResourceObject](docs/NetworkDetailsResourceObject.md)
 - [NetworkDetailsResourceObjectLinks](docs/NetworkDetailsResourceObjectLinks.md)
 - [NetworkInfoReadMultiple](docs/NetworkInfoReadMultiple.md)
 - [NetworkInfoReadMultipleLinks](docs/NetworkInfoReadMultipleLinks.md)
 - [NetworkInfoReadSingle](docs/NetworkInfoReadSingle.md)
 - [NetworkRelationships](docs/NetworkRelationships.md)
 - [NetworkRelationshipsDevices](docs/NetworkRelationshipsDevices.md)
 - [NetworkRelationshipsDevicesAttributes](docs/NetworkRelationshipsDevicesAttributes.md)
 - [NetworkRelationshipsDevicesData](docs/NetworkRelationshipsDevicesData.md)
 - [NetworkRelationshipsDevicesLinks](docs/NetworkRelationshipsDevicesLinks.md)
 - [NetworkRelationshipsNetworkDetail](docs/NetworkRelationshipsNetworkDetail.md)
 - [NetworkRelationshipsNetworkDetailData](docs/NetworkRelationshipsNetworkDetailData.md)
 - [NetworkRelationshipsNetworkDetailDataLinks](docs/NetworkRelationshipsNetworkDetailDataLinks.md)
 - [NetworksResourceObject](docs/NetworksResourceObject.md)
 - [NetworksResourceObjectLinks](docs/NetworksResourceObjectLinks.md)
 - [NoteAttributes](docs/NoteAttributes.md)
 - [NoteRelationships](docs/NoteRelationships.md)
 - [NoteResourceObject](docs/NoteResourceObject.md)
 - [NoteResourceObjectLinks](docs/NoteResourceObjectLinks.md)
 - [OidAttributes](docs/OidAttributes.md)
 - [OidRelationships](docs/OidRelationships.md)
 - [OidRelationshipsDevice](docs/OidRelationshipsDevice.md)
 - [OidRelationshipsDeviceData](docs/OidRelationshipsDeviceData.md)
 - [ReportPeriod](docs/ReportPeriod.md)
 - [ServiceStatisticsAttributes](docs/ServiceStatisticsAttributes.md)
 - [ServiceStatisticsRead](docs/ServiceStatisticsRead.md)
 - [ServiceStatisticsRelationships](docs/ServiceStatisticsRelationships.md)
 - [ServiceStatisticsRelationshipsService](docs/ServiceStatisticsRelationshipsService.md)
 - [ServiceStatisticsRelationshipsServiceData](docs/ServiceStatisticsRelationshipsServiceData.md)
 - [ServiceStatisticsRelationshipsServiceDataAttributes](docs/ServiceStatisticsRelationshipsServiceDataAttributes.md)
 - [ServiceStatisticsRelationshipsServiceDataLinks](docs/ServiceStatisticsRelationshipsServiceDataLinks.md)
 - [ServiceStatisticsResourceObject](docs/ServiceStatisticsResourceObject.md)
 - [ServiceStatisticsResourceObjectLinks](docs/ServiceStatisticsResourceObjectLinks.md)
 - [SnmpPollerIntHistoryAttributes](docs/SnmpPollerIntHistoryAttributes.md)
 - [SnmpPollerIntHistoryRead](docs/SnmpPollerIntHistoryRead.md)
 - [SnmpPollerIntHistoryReadLinks](docs/SnmpPollerIntHistoryReadLinks.md)
 - [SnmpPollerIntHistoryRelationships](docs/SnmpPollerIntHistoryRelationships.md)
 - [SnmpPollerIntHistoryResourceObject](docs/SnmpPollerIntHistoryResourceObject.md)
 - [SnmpPollerSetting](docs/SnmpPollerSetting.md)
 - [SnmpPollerSettingAttributes](docs/SnmpPollerSettingAttributes.md)
 - [SnmpPollerSettingAttributes2](docs/SnmpPollerSettingAttributes2.md)
 - [SnmpPollerSettingData](docs/SnmpPollerSettingData.md)
 - [SnmpPollerSettingDataAttributes](docs/SnmpPollerSettingDataAttributes.md)
 - [SnmpPollerSettingDeviceAttributes](docs/SnmpPollerSettingDeviceAttributes.md)
 - [SnmpPollerSettingDeviceRelationships](docs/SnmpPollerSettingDeviceRelationships.md)
 - [SnmpPollerSettingDeviceResourceObject](docs/SnmpPollerSettingDeviceResourceObject.md)
 - [SnmpPollerSettingDeviceResourceObjectLinks](docs/SnmpPollerSettingDeviceResourceObjectLinks.md)
 - [SnmpPollerSettingDevicesRead](docs/SnmpPollerSettingDevicesRead.md)
 - [SnmpPollerSettingDevicesReadLinks](docs/SnmpPollerSettingDevicesReadLinks.md)
 - [SnmpPollerSettingReduced](docs/SnmpPollerSettingReduced.md)
 - [SnmpPollerSettingReducedData](docs/SnmpPollerSettingReducedData.md)
 - [SnmpPollerSettingRelationships](docs/SnmpPollerSettingRelationships.md)
 - [SnmpPollerSettingRelationships2](docs/SnmpPollerSettingRelationships2.md)
 - [SnmpPollerSettingSingleRead](docs/SnmpPollerSettingSingleRead.md)
 - [SnmpPollerSettingSingleResourceObject](docs/SnmpPollerSettingSingleResourceObject.md)
 - [SnmpPollerSettingsRead](docs/SnmpPollerSettingsRead.md)
 - [SnmpPollerSettingsReadLinks](docs/SnmpPollerSettingsReadLinks.md)
 - [SnmpPollerSettingsResourceObject](docs/SnmpPollerSettingsResourceObject.md)
 - [SnmpPollerStringHistoryAttributes](docs/SnmpPollerStringHistoryAttributes.md)
 - [SnmpPollerStringHistoryAttributesReportPeriod](docs/SnmpPollerStringHistoryAttributesReportPeriod.md)
 - [SnmpPollerStringHistoryRead](docs/SnmpPollerStringHistoryRead.md)
 - [SnmpPollerStringHistoryReadLinks](docs/SnmpPollerStringHistoryReadLinks.md)
 - [SnmpPollerStringHistoryRelationships](docs/SnmpPollerStringHistoryRelationships.md)
 - [SnmpPollerStringHistoryResourceObject](docs/SnmpPollerStringHistoryResourceObject.md)
 - [Stack](docs/Stack.md)
 - [StackAllOfAttributes](docs/StackAllOfAttributes.md)
 - [StackAllOfRelationships](docs/StackAllOfRelationships.md)
 - [StackAllOfRelationshipsAllOfMembersInner](docs/StackAllOfRelationshipsAllOfMembersInner.md)
 - [StackAllOfRelationshipsAllOfMembersInnerAttributes](docs/StackAllOfRelationshipsAllOfMembersInnerAttributes.md)
 - [StackAllOfRelationshipsAllOfMembersInnerLinks](docs/StackAllOfRelationshipsAllOfMembersInnerLinks.md)
 - [StatItem](docs/StatItem.md)
 - [StatItem2](docs/StatItem2.md)
 - [StatItem2DataInnerInner](docs/StatItem2DataInnerInner.md)
 - [StatisticsAttributes](docs/StatisticsAttributes.md)
 - [Tenant](docs/Tenant.md)
 - [TenantAttributes](docs/TenantAttributes.md)
 - [TenantData](docs/TenantData.md)
 - [TenantDataAttributes](docs/TenantDataAttributes.md)
 - [TenantDetailAttributes](docs/TenantDetailAttributes.md)
 - [TenantDetailAttributesAddress](docs/TenantDetailAttributesAddress.md)
 - [TenantDetailResourceObject](docs/TenantDetailResourceObject.md)
 - [TenantDetailResourceObjectRelationships](docs/TenantDetailResourceObjectRelationships.md)
 - [TenantDetailResourceObjectRelationshipsAuthorizations](docs/TenantDetailResourceObjectRelationshipsAuthorizations.md)
 - [TenantDetailResourceObjectRelationshipsAuthorizationsData](docs/TenantDetailResourceObjectRelationshipsAuthorizationsData.md)
 - [TenantDetailResourceObjectRelationshipsParent](docs/TenantDetailResourceObjectRelationshipsParent.md)
 - [TenantDetailResourceObjectRelationshipsParentData](docs/TenantDetailResourceObjectRelationshipsParentData.md)
 - [TenantReduced](docs/TenantReduced.md)
 - [TenantReducedData](docs/TenantReducedData.md)
 - [TenantsDetailReadMultiple](docs/TenantsDetailReadMultiple.md)
 - [TenantsDetailReadSingle](docs/TenantsDetailReadSingle.md)
 - [TenantsResourceObject](docs/TenantsResourceObject.md)
 - [TenantsResourceObjectRelationships](docs/TenantsResourceObjectRelationships.md)
 - [TenantsResourceObjectRelationshipsParent](docs/TenantsResourceObjectRelationshipsParent.md)
 - [TenantsResourceObjectRelationshipsParentData](docs/TenantsResourceObjectRelationshipsParentData.md)
 - [UserTenantsReadMultiple](docs/UserTenantsReadMultiple.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKey"></a>
### ApiKey

- **Type**: HTTP basic authentication


## Author





# coding: utf-8

# flake8: noqa
"""
    Auvik API

    To use the Auvik APIs, you’ll need a <a href=\"https://support.auvik.com/hc/en-us/articles/204309114-#topic_generate\" target=\"_blank\">valid Auvik user and the user’s API key</a>. The user must also have the correct <a href=\" https://support.auvik.com/hc/en-us/articles/115002815966\" target=\"_blank\">role permissions</a>.<br>     <br>     Note: The word <i>tenant</i> as it appears in the API descriptions means one of Auvik’s supported tenant types: multi-client or client.<br><br>All date formats are formatted in the format of YYYY-MM-DDTHH:MM:SS.sssZ, as describe in ISO 8061<br><br>To find out more about Auvik’s APIs, <a href=\"https://support.auvik.com/hc/en-us/articles/360017965092\" target=\"_blank\">click here.</a>

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from layer8_auvik_api_client.models.access_point import AccessPoint
from layer8_auvik_api_client.models.access_point_all_of_attributes import AccessPointAllOfAttributes
from layer8_auvik_api_client.models.access_point_all_of_relationships import AccessPointAllOfRelationships
from layer8_auvik_api_client.models.access_point_all_of_relationships_all_of_wireless_clients_inner import AccessPointAllOfRelationshipsAllOfWirelessClientsInner
from layer8_auvik_api_client.models.access_point_all_of_relationships_all_of_wireless_clients_inner_attributes import AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes
from layer8_auvik_api_client.models.alert_attributes import AlertAttributes
from layer8_auvik_api_client.models.alert_attributes_external_ticket import AlertAttributesExternalTicket
from layer8_auvik_api_client.models.alert_history_info_read_multiple import AlertHistoryInfoReadMultiple
from layer8_auvik_api_client.models.alert_history_info_read_multiple_links import AlertHistoryInfoReadMultipleLinks
from layer8_auvik_api_client.models.alert_history_info_read_single import AlertHistoryInfoReadSingle
from layer8_auvik_api_client.models.alert_relationships import AlertRelationships
from layer8_auvik_api_client.models.alert_relationships_entity import AlertRelationshipsEntity
from layer8_auvik_api_client.models.alert_relationships_entity_data import AlertRelationshipsEntityData
from layer8_auvik_api_client.models.alert_relationships_entity_data_links import AlertRelationshipsEntityDataLinks
from layer8_auvik_api_client.models.alert_relationships_related_alert import AlertRelationshipsRelatedAlert
from layer8_auvik_api_client.models.alert_relationships_related_alert_data import AlertRelationshipsRelatedAlertData
from layer8_auvik_api_client.models.alert_relationships_related_alert_data_attributes import AlertRelationshipsRelatedAlertDataAttributes
from layer8_auvik_api_client.models.alert_relationships_related_alert_data_links import AlertRelationshipsRelatedAlertDataLinks
from layer8_auvik_api_client.models.alerts_resource_object import AlertsResourceObject
from layer8_auvik_api_client.models.alerts_resource_object_links import AlertsResourceObjectLinks
from layer8_auvik_api_client.models.audit_attributes import AuditAttributes
from layer8_auvik_api_client.models.audit_relationships import AuditRelationships
from layer8_auvik_api_client.models.audit_relationships_device import AuditRelationshipsDevice
from layer8_auvik_api_client.models.audit_relationships_device_data import AuditRelationshipsDeviceData
from layer8_auvik_api_client.models.audit_relationships_device_data_attributes import AuditRelationshipsDeviceDataAttributes
from layer8_auvik_api_client.models.audits_resource_object import AuditsResourceObject
from layer8_auvik_api_client.models.audits_resource_object_links import AuditsResourceObjectLinks
from layer8_auvik_api_client.models.base_device_extended_details_attributes import BaseDeviceExtendedDetailsAttributes
from layer8_auvik_api_client.models.basic_error import BasicError
from layer8_auvik_api_client.models.client_usage_attributes import ClientUsageAttributes
from layer8_auvik_api_client.models.client_usage_attributes_client_usage import ClientUsageAttributesClientUsage
from layer8_auvik_api_client.models.client_usage_attributes_client_usage_average_days_by_client_type import ClientUsageAttributesClientUsageAverageDaysByClientType
from layer8_auvik_api_client.models.client_usage_attributes_client_usage_total_days_by_client_type import ClientUsageAttributesClientUsageTotalDaysByClientType
from layer8_auvik_api_client.models.client_usage_attributes_device_usage import ClientUsageAttributesDeviceUsage
from layer8_auvik_api_client.models.client_usage_attributes_device_usage_average_days_by_client_type import ClientUsageAttributesDeviceUsageAverageDaysByClientType
from layer8_auvik_api_client.models.client_usage_attributes_device_usage_total_days_by_client_type import ClientUsageAttributesDeviceUsageTotalDaysByClientType
from layer8_auvik_api_client.models.client_usage_attributes_usage_period import ClientUsageAttributesUsagePeriod
from layer8_auvik_api_client.models.client_usage_read import ClientUsageRead
from layer8_auvik_api_client.models.client_usage_relationships import ClientUsageRelationships
from layer8_auvik_api_client.models.client_usage_relationships_clients import ClientUsageRelationshipsClients
from layer8_auvik_api_client.models.client_usage_relationships_clients_attributes import ClientUsageRelationshipsClientsAttributes
from layer8_auvik_api_client.models.client_usage_relationships_clients_data import ClientUsageRelationshipsClientsData
from layer8_auvik_api_client.models.client_usage_relationships_clients_links import ClientUsageRelationshipsClientsLinks
from layer8_auvik_api_client.models.client_usage_relationships_devices import ClientUsageRelationshipsDevices
from layer8_auvik_api_client.models.client_usage_relationships_devices_attributes import ClientUsageRelationshipsDevicesAttributes
from layer8_auvik_api_client.models.client_usage_relationships_devices_data import ClientUsageRelationshipsDevicesData
from layer8_auvik_api_client.models.client_usage_relationships_devices_links import ClientUsageRelationshipsDevicesLinks
from layer8_auvik_api_client.models.client_usage_resource_object import ClientUsageResourceObject
from layer8_auvik_api_client.models.client_usage_resource_object_links import ClientUsageResourceObjectLinks
from layer8_auvik_api_client.models.component_attributes import ComponentAttributes
from layer8_auvik_api_client.models.component_info_read_multiple import ComponentInfoReadMultiple
from layer8_auvik_api_client.models.component_info_read_multiple_links import ComponentInfoReadMultipleLinks
from layer8_auvik_api_client.models.component_info_read_single import ComponentInfoReadSingle
from layer8_auvik_api_client.models.component_relationships import ComponentRelationships
from layer8_auvik_api_client.models.component_relationships_parent_device import ComponentRelationshipsParentDevice
from layer8_auvik_api_client.models.component_relationships_parent_device_data import ComponentRelationshipsParentDeviceData
from layer8_auvik_api_client.models.component_statistics_read import ComponentStatisticsRead
from layer8_auvik_api_client.models.component_statistics_relationships import ComponentStatisticsRelationships
from layer8_auvik_api_client.models.component_statistics_relationships_component import ComponentStatisticsRelationshipsComponent
from layer8_auvik_api_client.models.component_statistics_relationships_component_data import ComponentStatisticsRelationshipsComponentData
from layer8_auvik_api_client.models.component_statistics_relationships_component_data_links import ComponentStatisticsRelationshipsComponentDataLinks
from layer8_auvik_api_client.models.component_statistics_resource_object import ComponentStatisticsResourceObject
from layer8_auvik_api_client.models.component_statistics_resource_object_links import ComponentStatisticsResourceObjectLinks
from layer8_auvik_api_client.models.components_resource_object import ComponentsResourceObject
from layer8_auvik_api_client.models.components_resource_object_links import ComponentsResourceObjectLinks
from layer8_auvik_api_client.models.config_attributes import ConfigAttributes
from layer8_auvik_api_client.models.config_read_multiple import ConfigReadMultiple
from layer8_auvik_api_client.models.config_read_multiple_links import ConfigReadMultipleLinks
from layer8_auvik_api_client.models.config_read_single import ConfigReadSingle
from layer8_auvik_api_client.models.config_relationships import ConfigRelationships
from layer8_auvik_api_client.models.config_resource_object import ConfigResourceObject
from layer8_auvik_api_client.models.config_resource_object_links import ConfigResourceObjectLinks
from layer8_auvik_api_client.models.controller import Controller
from layer8_auvik_api_client.models.controller_all_of_attributes import ControllerAllOfAttributes
from layer8_auvik_api_client.models.controller_all_of_relationships import ControllerAllOfRelationships
from layer8_auvik_api_client.models.controller_all_of_relationships_all_of_access_points_inner import ControllerAllOfRelationshipsAllOfAccessPointsInner
from layer8_auvik_api_client.models.controller_all_of_relationships_all_of_access_points_inner_attributes import ControllerAllOfRelationshipsAllOfAccessPointsInnerAttributes
from layer8_auvik_api_client.models.controller_all_of_relationships_all_of_access_points_inner_links import ControllerAllOfRelationshipsAllOfAccessPointsInnerLinks
from layer8_auvik_api_client.models.device import Device
from layer8_auvik_api_client.models.device_attributes import DeviceAttributes
from layer8_auvik_api_client.models.device_availability_statistics_read import DeviceAvailabilityStatisticsRead
from layer8_auvik_api_client.models.device_availability_statistics_resource_object import DeviceAvailabilityStatisticsResourceObject
from layer8_auvik_api_client.models.device_data import DeviceData
from layer8_auvik_api_client.models.device_details_attributes import DeviceDetailsAttributes
from layer8_auvik_api_client.models.device_details_attributes_discovery_status import DeviceDetailsAttributesDiscoveryStatus
from layer8_auvik_api_client.models.device_details_extended_read_multiple import DeviceDetailsExtendedReadMultiple
from layer8_auvik_api_client.models.device_details_extended_read_multiple_links import DeviceDetailsExtendedReadMultipleLinks
from layer8_auvik_api_client.models.device_details_extended_read_single import DeviceDetailsExtendedReadSingle
from layer8_auvik_api_client.models.device_details_read_multiple import DeviceDetailsReadMultiple
from layer8_auvik_api_client.models.device_details_read_multiple_links import DeviceDetailsReadMultipleLinks
from layer8_auvik_api_client.models.device_details_read_single import DeviceDetailsReadSingle
from layer8_auvik_api_client.models.device_details_relationships import DeviceDetailsRelationships
from layer8_auvik_api_client.models.device_details_relationships_components import DeviceDetailsRelationshipsComponents
from layer8_auvik_api_client.models.device_details_relationships_components_attributes import DeviceDetailsRelationshipsComponentsAttributes
from layer8_auvik_api_client.models.device_details_relationships_components_data import DeviceDetailsRelationshipsComponentsData
from layer8_auvik_api_client.models.device_details_relationships_components_links import DeviceDetailsRelationshipsComponentsLinks
from layer8_auvik_api_client.models.device_details_relationships_configurations import DeviceDetailsRelationshipsConfigurations
from layer8_auvik_api_client.models.device_details_relationships_configurations_attributes import DeviceDetailsRelationshipsConfigurationsAttributes
from layer8_auvik_api_client.models.device_details_relationships_configurations_data import DeviceDetailsRelationshipsConfigurationsData
from layer8_auvik_api_client.models.device_details_relationships_configurations_links import DeviceDetailsRelationshipsConfigurationsLinks
from layer8_auvik_api_client.models.device_details_relationships_connected_devices import DeviceDetailsRelationshipsConnectedDevices
from layer8_auvik_api_client.models.device_details_relationships_connected_devices_attributes import DeviceDetailsRelationshipsConnectedDevicesAttributes
from layer8_auvik_api_client.models.device_details_relationships_connected_devices_data import DeviceDetailsRelationshipsConnectedDevicesData
from layer8_auvik_api_client.models.device_details_relationships_connected_devices_links import DeviceDetailsRelationshipsConnectedDevicesLinks
from layer8_auvik_api_client.models.device_details_relationships_interfaces import DeviceDetailsRelationshipsInterfaces
from layer8_auvik_api_client.models.device_details_relationships_interfaces_attributes import DeviceDetailsRelationshipsInterfacesAttributes
from layer8_auvik_api_client.models.device_details_relationships_interfaces_data import DeviceDetailsRelationshipsInterfacesData
from layer8_auvik_api_client.models.device_details_relationships_interfaces_links import DeviceDetailsRelationshipsInterfacesLinks
from layer8_auvik_api_client.models.device_details_resource_object import DeviceDetailsResourceObject
from layer8_auvik_api_client.models.device_details_resource_object_links import DeviceDetailsResourceObjectLinks
from layer8_auvik_api_client.models.device_extended_detail_resource_object import DeviceExtendedDetailResourceObject
from layer8_auvik_api_client.models.device_extended_details_device import DeviceExtendedDetailsDevice
from layer8_auvik_api_client.models.device_extended_details_device_links import DeviceExtendedDetailsDeviceLinks
from layer8_auvik_api_client.models.device_info_read_multiple import DeviceInfoReadMultiple
from layer8_auvik_api_client.models.device_info_read_multiple_links import DeviceInfoReadMultipleLinks
from layer8_auvik_api_client.models.device_info_read_single import DeviceInfoReadSingle
from layer8_auvik_api_client.models.device_lifecycle_attributes import DeviceLifecycleAttributes
from layer8_auvik_api_client.models.device_lifecycle_read_multiple import DeviceLifecycleReadMultiple
from layer8_auvik_api_client.models.device_lifecycle_read_multiple_links import DeviceLifecycleReadMultipleLinks
from layer8_auvik_api_client.models.device_lifecycle_read_single import DeviceLifecycleReadSingle
from layer8_auvik_api_client.models.device_lifecycle_relationships import DeviceLifecycleRelationships
from layer8_auvik_api_client.models.device_lifecycle_relationships_device import DeviceLifecycleRelationshipsDevice
from layer8_auvik_api_client.models.device_lifecycle_relationships_device_data import DeviceLifecycleRelationshipsDeviceData
from layer8_auvik_api_client.models.device_lifecycle_relationships_device_data_attributes import DeviceLifecycleRelationshipsDeviceDataAttributes
from layer8_auvik_api_client.models.device_lifecycle_resource_object import DeviceLifecycleResourceObject
from layer8_auvik_api_client.models.device_lifecycle_resource_object_links import DeviceLifecycleResourceObjectLinks
from layer8_auvik_api_client.models.device_oid_monitor_read import DeviceOidMonitorRead
from layer8_auvik_api_client.models.device_oid_monitor_read_links import DeviceOidMonitorReadLinks
from layer8_auvik_api_client.models.device_oid_monitor_resource_object import DeviceOidMonitorResourceObject
from layer8_auvik_api_client.models.device_oid_monitor_resource_object_links import DeviceOidMonitorResourceObjectLinks
from layer8_auvik_api_client.models.device_relationships import DeviceRelationships
from layer8_auvik_api_client.models.device_relationships_device_detail import DeviceRelationshipsDeviceDetail
from layer8_auvik_api_client.models.device_relationships_device_detail_data import DeviceRelationshipsDeviceDetailData
from layer8_auvik_api_client.models.device_relationships_device_detail_data_links import DeviceRelationshipsDeviceDetailDataLinks
from layer8_auvik_api_client.models.device_relationships_networks import DeviceRelationshipsNetworks
from layer8_auvik_api_client.models.device_relationships_networks_attributes import DeviceRelationshipsNetworksAttributes
from layer8_auvik_api_client.models.device_relationships_networks_data import DeviceRelationshipsNetworksData
from layer8_auvik_api_client.models.device_relationships_networks_links import DeviceRelationshipsNetworksLinks
from layer8_auvik_api_client.models.device_statistics_read import DeviceStatisticsRead
from layer8_auvik_api_client.models.device_statistics_relationships import DeviceStatisticsRelationships
from layer8_auvik_api_client.models.device_statistics_relationships_device import DeviceStatisticsRelationshipsDevice
from layer8_auvik_api_client.models.device_statistics_relationships_device_data import DeviceStatisticsRelationshipsDeviceData
from layer8_auvik_api_client.models.device_statistics_resource_object import DeviceStatisticsResourceObject
from layer8_auvik_api_client.models.device_statistics_resource_object_links import DeviceStatisticsResourceObjectLinks
from layer8_auvik_api_client.models.device_type_schema import DeviceTypeSchema
from layer8_auvik_api_client.models.device_usage_attributes import DeviceUsageAttributes
from layer8_auvik_api_client.models.device_usage_attributes_average_days_by_client_type import DeviceUsageAttributesAverageDaysByClientType
from layer8_auvik_api_client.models.device_usage_attributes_total_days_by_client_type import DeviceUsageAttributesTotalDaysByClientType
from layer8_auvik_api_client.models.device_usage_read import DeviceUsageRead
from layer8_auvik_api_client.models.device_usage_relationships import DeviceUsageRelationships
from layer8_auvik_api_client.models.device_usage_relationships_client import DeviceUsageRelationshipsClient
from layer8_auvik_api_client.models.device_usage_relationships_client_data import DeviceUsageRelationshipsClientData
from layer8_auvik_api_client.models.device_usage_relationships_client_data_attributes import DeviceUsageRelationshipsClientDataAttributes
from layer8_auvik_api_client.models.device_usage_resource_object import DeviceUsageResourceObject
from layer8_auvik_api_client.models.device_usage_resource_object_links import DeviceUsageResourceObjectLinks
from layer8_auvik_api_client.models.device_warranty_attributes import DeviceWarrantyAttributes
from layer8_auvik_api_client.models.device_warranty_read_multiple import DeviceWarrantyReadMultiple
from layer8_auvik_api_client.models.device_warranty_read_multiple_links import DeviceWarrantyReadMultipleLinks
from layer8_auvik_api_client.models.device_warranty_read_single import DeviceWarrantyReadSingle
from layer8_auvik_api_client.models.device_warranty_relationships import DeviceWarrantyRelationships
from layer8_auvik_api_client.models.device_warranty_resource_object import DeviceWarrantyResourceObject
from layer8_auvik_api_client.models.device_warranty_resource_object_links import DeviceWarrantyResourceObjectLinks
from layer8_auvik_api_client.models.devices_resource_object import DevicesResourceObject
from layer8_auvik_api_client.models.devices_resource_object_links import DevicesResourceObjectLinks
from layer8_auvik_api_client.models.endpoint_stats import EndpointStats
from layer8_auvik_api_client.models.entity_audit_read_multiple import EntityAuditReadMultiple
from layer8_auvik_api_client.models.entity_audit_read_multiple_links import EntityAuditReadMultipleLinks
from layer8_auvik_api_client.models.entity_audit_read_single import EntityAuditReadSingle
from layer8_auvik_api_client.models.entity_notes_read_multiple import EntityNotesReadMultiple
from layer8_auvik_api_client.models.entity_notes_read_multiple_links import EntityNotesReadMultipleLinks
from layer8_auvik_api_client.models.entity_notes_read_single import EntityNotesReadSingle
from layer8_auvik_api_client.models.hypervisor import Hypervisor
from layer8_auvik_api_client.models.hypervisor_all_of_attributes import HypervisorAllOfAttributes
from layer8_auvik_api_client.models.hypervisor_all_of_attributes_all_of_virtual_machines_inner import HypervisorAllOfAttributesAllOfVirtualMachinesInner
from layer8_auvik_api_client.models.hypervisor_all_of_attributes_all_of_virtual_machines_inner_snapshots_inner import HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner
from layer8_auvik_api_client.models.interface_attributes import InterfaceAttributes
from layer8_auvik_api_client.models.interface_info_read_multiple import InterfaceInfoReadMultiple
from layer8_auvik_api_client.models.interface_info_read_multiple_links import InterfaceInfoReadMultipleLinks
from layer8_auvik_api_client.models.interface_info_read_single import InterfaceInfoReadSingle
from layer8_auvik_api_client.models.interface_relationships import InterfaceRelationships
from layer8_auvik_api_client.models.interface_relationships_connected_to import InterfaceRelationshipsConnectedTo
from layer8_auvik_api_client.models.interface_relationships_connected_to_data import InterfaceRelationshipsConnectedToData
from layer8_auvik_api_client.models.interface_relationships_connected_to_links import InterfaceRelationshipsConnectedToLinks
from layer8_auvik_api_client.models.interface_relationships_networks import InterfaceRelationshipsNetworks
from layer8_auvik_api_client.models.interface_relationships_networks_data import InterfaceRelationshipsNetworksData
from layer8_auvik_api_client.models.interface_relationships_networks_links import InterfaceRelationshipsNetworksLinks
from layer8_auvik_api_client.models.interface_relationships_parent_device import InterfaceRelationshipsParentDevice
from layer8_auvik_api_client.models.interface_relationships_parent_device_data import InterfaceRelationshipsParentDeviceData
from layer8_auvik_api_client.models.interface_relationships_parent_device_data_links import InterfaceRelationshipsParentDeviceDataLinks
from layer8_auvik_api_client.models.interface_resource_object import InterfaceResourceObject
from layer8_auvik_api_client.models.interface_resource_object_links import InterfaceResourceObjectLinks
from layer8_auvik_api_client.models.interface_statistics_read import InterfaceStatisticsRead
from layer8_auvik_api_client.models.interface_statistics_relationships import InterfaceStatisticsRelationships
from layer8_auvik_api_client.models.interface_statistics_relationships_interface import InterfaceStatisticsRelationshipsInterface
from layer8_auvik_api_client.models.interface_statistics_relationships_interface_data import InterfaceStatisticsRelationshipsInterfaceData
from layer8_auvik_api_client.models.interface_statistics_relationships_interface_data_links import InterfaceStatisticsRelationshipsInterfaceDataLinks
from layer8_auvik_api_client.models.interface_statistics_resource_object import InterfaceStatisticsResourceObject
from layer8_auvik_api_client.models.interface_statistics_resource_object_links import InterfaceStatisticsResourceObjectLinks
from layer8_auvik_api_client.models.meta import Meta
from layer8_auvik_api_client.models.misc_device import MiscDevice
from layer8_auvik_api_client.models.misc_device_all_of_attributes import MiscDeviceAllOfAttributes
from layer8_auvik_api_client.models.misc_device_all_of_attributes_all_of_tunnels_inner import MiscDeviceAllOfAttributesAllOfTunnelsInner
from layer8_auvik_api_client.models.network_attributes import NetworkAttributes
from layer8_auvik_api_client.models.network_details_attributes import NetworkDetailsAttributes
from layer8_auvik_api_client.models.network_details_read_multiple import NetworkDetailsReadMultiple
from layer8_auvik_api_client.models.network_details_read_multiple_links import NetworkDetailsReadMultipleLinks
from layer8_auvik_api_client.models.network_details_read_single import NetworkDetailsReadSingle
from layer8_auvik_api_client.models.network_details_relationships import NetworkDetailsRelationships
from layer8_auvik_api_client.models.network_details_resource_object import NetworkDetailsResourceObject
from layer8_auvik_api_client.models.network_details_resource_object_links import NetworkDetailsResourceObjectLinks
from layer8_auvik_api_client.models.network_info_read_multiple import NetworkInfoReadMultiple
from layer8_auvik_api_client.models.network_info_read_multiple_links import NetworkInfoReadMultipleLinks
from layer8_auvik_api_client.models.network_info_read_single import NetworkInfoReadSingle
from layer8_auvik_api_client.models.network_relationships import NetworkRelationships
from layer8_auvik_api_client.models.network_relationships_devices import NetworkRelationshipsDevices
from layer8_auvik_api_client.models.network_relationships_devices_attributes import NetworkRelationshipsDevicesAttributes
from layer8_auvik_api_client.models.network_relationships_devices_data import NetworkRelationshipsDevicesData
from layer8_auvik_api_client.models.network_relationships_devices_links import NetworkRelationshipsDevicesLinks
from layer8_auvik_api_client.models.network_relationships_network_detail import NetworkRelationshipsNetworkDetail
from layer8_auvik_api_client.models.network_relationships_network_detail_data import NetworkRelationshipsNetworkDetailData
from layer8_auvik_api_client.models.network_relationships_network_detail_data_links import NetworkRelationshipsNetworkDetailDataLinks
from layer8_auvik_api_client.models.networks_resource_object import NetworksResourceObject
from layer8_auvik_api_client.models.networks_resource_object_links import NetworksResourceObjectLinks
from layer8_auvik_api_client.models.note_attributes import NoteAttributes
from layer8_auvik_api_client.models.note_relationships import NoteRelationships
from layer8_auvik_api_client.models.note_resource_object import NoteResourceObject
from layer8_auvik_api_client.models.note_resource_object_links import NoteResourceObjectLinks
from layer8_auvik_api_client.models.oid_attributes import OidAttributes
from layer8_auvik_api_client.models.oid_relationships import OidRelationships
from layer8_auvik_api_client.models.oid_relationships_device import OidRelationshipsDevice
from layer8_auvik_api_client.models.oid_relationships_device_data import OidRelationshipsDeviceData
from layer8_auvik_api_client.models.report_period import ReportPeriod
from layer8_auvik_api_client.models.service_statistics_attributes import ServiceStatisticsAttributes
from layer8_auvik_api_client.models.service_statistics_read import ServiceStatisticsRead
from layer8_auvik_api_client.models.service_statistics_relationships import ServiceStatisticsRelationships
from layer8_auvik_api_client.models.service_statistics_relationships_service import ServiceStatisticsRelationshipsService
from layer8_auvik_api_client.models.service_statistics_relationships_service_data import ServiceStatisticsRelationshipsServiceData
from layer8_auvik_api_client.models.service_statistics_relationships_service_data_attributes import ServiceStatisticsRelationshipsServiceDataAttributes
from layer8_auvik_api_client.models.service_statistics_relationships_service_data_links import ServiceStatisticsRelationshipsServiceDataLinks
from layer8_auvik_api_client.models.service_statistics_resource_object import ServiceStatisticsResourceObject
from layer8_auvik_api_client.models.service_statistics_resource_object_links import ServiceStatisticsResourceObjectLinks
from layer8_auvik_api_client.models.snmp_poller_int_history_attributes import SnmpPollerIntHistoryAttributes
from layer8_auvik_api_client.models.snmp_poller_int_history_read import SnmpPollerIntHistoryRead
from layer8_auvik_api_client.models.snmp_poller_int_history_read_links import SnmpPollerIntHistoryReadLinks
from layer8_auvik_api_client.models.snmp_poller_int_history_relationships import SnmpPollerIntHistoryRelationships
from layer8_auvik_api_client.models.snmp_poller_int_history_resource_object import SnmpPollerIntHistoryResourceObject
from layer8_auvik_api_client.models.snmp_poller_setting import SnmpPollerSetting
from layer8_auvik_api_client.models.snmp_poller_setting_attributes import SnmpPollerSettingAttributes
from layer8_auvik_api_client.models.snmp_poller_setting_attributes2 import SnmpPollerSettingAttributes2
from layer8_auvik_api_client.models.snmp_poller_setting_data import SnmpPollerSettingData
from layer8_auvik_api_client.models.snmp_poller_setting_data_attributes import SnmpPollerSettingDataAttributes
from layer8_auvik_api_client.models.snmp_poller_setting_device_attributes import SnmpPollerSettingDeviceAttributes
from layer8_auvik_api_client.models.snmp_poller_setting_device_relationships import SnmpPollerSettingDeviceRelationships
from layer8_auvik_api_client.models.snmp_poller_setting_device_resource_object import SnmpPollerSettingDeviceResourceObject
from layer8_auvik_api_client.models.snmp_poller_setting_device_resource_object_links import SnmpPollerSettingDeviceResourceObjectLinks
from layer8_auvik_api_client.models.snmp_poller_setting_devices_read import SnmpPollerSettingDevicesRead
from layer8_auvik_api_client.models.snmp_poller_setting_devices_read_links import SnmpPollerSettingDevicesReadLinks
from layer8_auvik_api_client.models.snmp_poller_setting_reduced import SnmpPollerSettingReduced
from layer8_auvik_api_client.models.snmp_poller_setting_reduced_data import SnmpPollerSettingReducedData
from layer8_auvik_api_client.models.snmp_poller_setting_relationships import SnmpPollerSettingRelationships
from layer8_auvik_api_client.models.snmp_poller_setting_relationships2 import SnmpPollerSettingRelationships2
from layer8_auvik_api_client.models.snmp_poller_setting_single_read import SnmpPollerSettingSingleRead
from layer8_auvik_api_client.models.snmp_poller_setting_single_resource_object import SnmpPollerSettingSingleResourceObject
from layer8_auvik_api_client.models.snmp_poller_settings_read import SnmpPollerSettingsRead
from layer8_auvik_api_client.models.snmp_poller_settings_read_links import SnmpPollerSettingsReadLinks
from layer8_auvik_api_client.models.snmp_poller_settings_resource_object import SnmpPollerSettingsResourceObject
from layer8_auvik_api_client.models.snmp_poller_string_history_attributes import SnmpPollerStringHistoryAttributes
from layer8_auvik_api_client.models.snmp_poller_string_history_attributes_report_period import SnmpPollerStringHistoryAttributesReportPeriod
from layer8_auvik_api_client.models.snmp_poller_string_history_read import SnmpPollerStringHistoryRead
from layer8_auvik_api_client.models.snmp_poller_string_history_read_links import SnmpPollerStringHistoryReadLinks
from layer8_auvik_api_client.models.snmp_poller_string_history_relationships import SnmpPollerStringHistoryRelationships
from layer8_auvik_api_client.models.snmp_poller_string_history_resource_object import SnmpPollerStringHistoryResourceObject
from layer8_auvik_api_client.models.stack import Stack
from layer8_auvik_api_client.models.stack_all_of_attributes import StackAllOfAttributes
from layer8_auvik_api_client.models.stack_all_of_relationships import StackAllOfRelationships
from layer8_auvik_api_client.models.stack_all_of_relationships_all_of_members_inner import StackAllOfRelationshipsAllOfMembersInner
from layer8_auvik_api_client.models.stack_all_of_relationships_all_of_members_inner_attributes import StackAllOfRelationshipsAllOfMembersInnerAttributes
from layer8_auvik_api_client.models.stack_all_of_relationships_all_of_members_inner_links import StackAllOfRelationshipsAllOfMembersInnerLinks
from layer8_auvik_api_client.models.stat_item import StatItem
from layer8_auvik_api_client.models.stat_item2 import StatItem2
from layer8_auvik_api_client.models.stat_item2_data_inner_inner import StatItem2DataInnerInner
from layer8_auvik_api_client.models.statistics_attributes import StatisticsAttributes
from layer8_auvik_api_client.models.tenant import Tenant
from layer8_auvik_api_client.models.tenant_attributes import TenantAttributes
from layer8_auvik_api_client.models.tenant_data import TenantData
from layer8_auvik_api_client.models.tenant_data_attributes import TenantDataAttributes
from layer8_auvik_api_client.models.tenant_detail_attributes import TenantDetailAttributes
from layer8_auvik_api_client.models.tenant_detail_attributes_address import TenantDetailAttributesAddress
from layer8_auvik_api_client.models.tenant_detail_resource_object import TenantDetailResourceObject
from layer8_auvik_api_client.models.tenant_detail_resource_object_relationships import TenantDetailResourceObjectRelationships
from layer8_auvik_api_client.models.tenant_detail_resource_object_relationships_authorizations import TenantDetailResourceObjectRelationshipsAuthorizations
from layer8_auvik_api_client.models.tenant_detail_resource_object_relationships_authorizations_data import TenantDetailResourceObjectRelationshipsAuthorizationsData
from layer8_auvik_api_client.models.tenant_detail_resource_object_relationships_parent import TenantDetailResourceObjectRelationshipsParent
from layer8_auvik_api_client.models.tenant_detail_resource_object_relationships_parent_data import TenantDetailResourceObjectRelationshipsParentData
from layer8_auvik_api_client.models.tenant_reduced import TenantReduced
from layer8_auvik_api_client.models.tenant_reduced_data import TenantReducedData
from layer8_auvik_api_client.models.tenants_detail_read_multiple import TenantsDetailReadMultiple
from layer8_auvik_api_client.models.tenants_detail_read_single import TenantsDetailReadSingle
from layer8_auvik_api_client.models.tenants_resource_object import TenantsResourceObject
from layer8_auvik_api_client.models.tenants_resource_object_relationships import TenantsResourceObjectRelationships
from layer8_auvik_api_client.models.tenants_resource_object_relationships_parent import TenantsResourceObjectRelationshipsParent
from layer8_auvik_api_client.models.tenants_resource_object_relationships_parent_data import TenantsResourceObjectRelationshipsParentData
from layer8_auvik_api_client.models.user_tenants_read_multiple import UserTenantsReadMultiple

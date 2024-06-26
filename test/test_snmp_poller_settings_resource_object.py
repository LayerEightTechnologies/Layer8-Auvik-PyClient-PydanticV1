# coding: utf-8

"""
    Auvik API

    To use the Auvik APIs, you’ll need a <a href=\"https://support.auvik.com/hc/en-us/articles/204309114-#topic_generate\" target=\"_blank\">valid Auvik user and the user’s API key</a>. The user must also have the correct <a href=\" https://support.auvik.com/hc/en-us/articles/115002815966\" target=\"_blank\">role permissions</a>.<br>     <br>     Note: The word <i>tenant</i> as it appears in the API descriptions means one of Auvik’s supported tenant types: multi-client or client.<br><br>All date formats are formatted in the format of YYYY-MM-DDTHH:MM:SS.sssZ, as describe in ISO 8061<br><br>To find out more about Auvik’s APIs, <a href=\"https://support.auvik.com/hc/en-us/articles/360017965092\" target=\"_blank\">click here.</a>

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from layer8_auvik_api_client.models.snmp_poller_settings_resource_object import SnmpPollerSettingsResourceObject  # noqa: E501

class TestSnmpPollerSettingsResourceObject(unittest.TestCase):
    """SnmpPollerSettingsResourceObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnmpPollerSettingsResourceObject:
        """Test SnmpPollerSettingsResourceObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnmpPollerSettingsResourceObject`
        """
        model = SnmpPollerSettingsResourceObject()  # noqa: E501
        if include_optional:
            return SnmpPollerSettingsResourceObject(
                id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw',
                type = 'snmpPollerSetting',
                attributes = layer8_auvik_api_client.models.snmp_poller_setting_attributes.snmpPollerSettingAttributes(
                    name = 'Cisco CPU Usage', 
                    protocol = 'snmp', 
                    oid = '1.3.6.1.4.1.17373.4.1.2.1.5.1', 
                    type = 'string', 
                    use_as = 'poller', ),
                relationships = layer8_auvik_api_client.models.snmp_poller_setting_relationships.snmpPollerSettingRelationships(
                    tenant = layer8_auvik_api_client.models.tenant.tenant(
                        data = layer8_auvik_api_client.models.tenant_data.tenant_data(
                            type = 'tenant', 
                            id = '195798545063742726', 
                            attributes = layer8_auvik_api_client.models.tenant_data_attributes.tenant_data_attributes(
                                domain_prefix = 'sampledomain', ), ), ), ),
                links = layer8_auvik_api_client.models.device_oid_monitor_resource_object_links.deviceOidMonitorResourceObject_links(
                    dashboard = 'https://sampledomain.my.auvik.com/#entity/oid/199502791112896003/dashboard', 
                    self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/oid/info/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', )
            )
        else:
            return SnmpPollerSettingsResourceObject(
        )
        """

    def testSnmpPollerSettingsResourceObject(self):
        """Test SnmpPollerSettingsResourceObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

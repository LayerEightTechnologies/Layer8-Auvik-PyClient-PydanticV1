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

from layer8_auvik_api_client.models.interface_resource_object import InterfaceResourceObject  # noqa: E501

class TestInterfaceResourceObject(unittest.TestCase):
    """InterfaceResourceObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterfaceResourceObject:
        """Test InterfaceResourceObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceResourceObject`
        """
        model = InterfaceResourceObject()  # noqa: E501
        if include_optional:
            return InterfaceResourceObject(
                type = 'interface',
                id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMjg5NjAwMw',
                attributes = layer8_auvik_api_client.models.interface_attributes.interfaceAttributes(
                    interface_name = 'Interface 1', 
                    interface_type = 'ethernet', 
                    mac_address = '1A:2B:3C:4D:5E:6F', 
                    negotiated_speed = '1.0 Gbit/s', 
                    duplex = 'full', 
                    custom_connections = True, 
                    ip_addresses = ["10.0.0.1"], 
                    operational_status = 'online', 
                    admin_status = True, 
                    last_modified = '2018-03-12T12:00:00.000Z', ),
                links = layer8_auvik_api_client.models.interface_resource_object_links.interfaceResourceObject_links(
                    dashboard = 'https://sampledomain.my.auvik.com/#entity/interface/199502791112896003/dashboard', 
                    self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/interface/info/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMjg5NjAwMw', ),
                relationships = layer8_auvik_api_client.models.interface_relationships.interfaceRelationships(
                    tenant = layer8_auvik_api_client.models.tenant.tenant(
                        data = layer8_auvik_api_client.models.tenant_data.tenant_data(
                            type = 'tenant', 
                            id = '195798545063742726', 
                            attributes = layer8_auvik_api_client.models.tenant_data_attributes.tenant_data_attributes(
                                domain_prefix = 'sampledomain', ), ), ), 
                    connected_to = layer8_auvik_api_client.models.interface_relationships_connected_to.interfaceRelationships_connectedTo(), 
                    networks = layer8_auvik_api_client.models.interface_relationships_networks.interfaceRelationships_networks(), 
                    parent_device = layer8_auvik_api_client.models.interface_relationships_parent_device.interfaceRelationships_parentDevice(), )
            )
        else:
            return InterfaceResourceObject(
        )
        """

    def testInterfaceResourceObject(self):
        """Test InterfaceResourceObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
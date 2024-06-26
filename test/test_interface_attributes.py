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

from layer8_auvik_api_client.models.interface_attributes import InterfaceAttributes  # noqa: E501

class TestInterfaceAttributes(unittest.TestCase):
    """InterfaceAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterfaceAttributes:
        """Test InterfaceAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceAttributes`
        """
        model = InterfaceAttributes()  # noqa: E501
        if include_optional:
            return InterfaceAttributes(
                interface_name = 'Interface 1',
                interface_type = 'ethernet',
                mac_address = '1A:2B:3C:4D:5E:6F',
                negotiated_speed = '1.0 Gbit/s',
                duplex = 'full',
                custom_connections = True,
                ip_addresses = ["10.0.0.1"],
                operational_status = 'online',
                admin_status = True,
                last_modified = '2018-03-12T12:00:00.000Z'
            )
        else:
            return InterfaceAttributes(
                interface_name = 'Interface 1',
                interface_type = 'ethernet',
                mac_address = '1A:2B:3C:4D:5E:6F',
                negotiated_speed = '1.0 Gbit/s',
                duplex = 'full',
                custom_connections = True,
                ip_addresses = ["10.0.0.1"],
                operational_status = 'online',
                admin_status = True,
                last_modified = '2018-03-12T12:00:00.000Z',
        )
        """

    def testInterfaceAttributes(self):
        """Test InterfaceAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

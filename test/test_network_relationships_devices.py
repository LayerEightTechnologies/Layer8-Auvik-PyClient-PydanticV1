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

from layer8_auvik_api_client.models.network_relationships_devices import NetworkRelationshipsDevices  # noqa: E501

class TestNetworkRelationshipsDevices(unittest.TestCase):
    """NetworkRelationshipsDevices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkRelationshipsDevices:
        """Test NetworkRelationshipsDevices
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkRelationshipsDevices`
        """
        model = NetworkRelationshipsDevices()  # noqa: E501
        if include_optional:
            return NetworkRelationshipsDevices(
                data = [
                    layer8_auvik_api_client.models.network_relationships_devices_data.networkRelationships_devices_data(
                        type = 'device', 
                        id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', 
                        attributes = layer8_auvik_api_client.models.network_relationships_devices_attributes.networkRelationships_devices_attributes(
                            device_name = 'MyAccessPoint', ), 
                        links = layer8_auvik_api_client.models.network_relationships_devices_links.networkRelationships_devices_links(
                            dashboard = 'https://sampledomain.my.auvik.com/#entity/device/199502791112896003/dashboard', 
                            self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/device/info/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', ), )
                    ]
            )
        else:
            return NetworkRelationshipsDevices(
        )
        """

    def testNetworkRelationshipsDevices(self):
        """Test NetworkRelationshipsDevices"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

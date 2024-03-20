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

from layer8_auvik_api_client.models.interface_relationships_connected_to import InterfaceRelationshipsConnectedTo  # noqa: E501

class TestInterfaceRelationshipsConnectedTo(unittest.TestCase):
    """InterfaceRelationshipsConnectedTo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterfaceRelationshipsConnectedTo:
        """Test InterfaceRelationshipsConnectedTo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceRelationshipsConnectedTo`
        """
        model = InterfaceRelationshipsConnectedTo()  # noqa: E501
        if include_optional:
            return InterfaceRelationshipsConnectedTo(
                data = [
                    layer8_auvik_api_client.models.interface_relationships_connected_to_data.interfaceRelationships_connectedTo_data(
                        id = 'MTk5NTAyNzg2ODc3MDYzNjgxLDE5OTUwMzc3Nzk1Njg4ODgzNQ', 
                        type = 'interface', 
                        links = layer8_auvik_api_client.models.interface_relationships_connected_to_links.interfaceRelationships_connectedTo_links(
                            dashboard = 'https://sampledomain.my.auvik.com/#entity/interface/199502791112896003/dashboard', 
                            self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/interface/info/MTk5NTAyNzg2ODc3MDYzNjgxLDE5OTUwMzc3Nzk1Njg4ODgzNQ', ), )
                    ]
            )
        else:
            return InterfaceRelationshipsConnectedTo(
        )
        """

    def testInterfaceRelationshipsConnectedTo(self):
        """Test InterfaceRelationshipsConnectedTo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

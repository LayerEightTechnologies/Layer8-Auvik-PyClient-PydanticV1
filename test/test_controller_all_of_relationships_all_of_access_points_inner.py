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

from layer8_auvik_api_client.models.controller_all_of_relationships_all_of_access_points_inner import ControllerAllOfRelationshipsAllOfAccessPointsInner  # noqa: E501

class TestControllerAllOfRelationshipsAllOfAccessPointsInner(unittest.TestCase):
    """ControllerAllOfRelationshipsAllOfAccessPointsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ControllerAllOfRelationshipsAllOfAccessPointsInner:
        """Test ControllerAllOfRelationshipsAllOfAccessPointsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ControllerAllOfRelationshipsAllOfAccessPointsInner`
        """
        model = ControllerAllOfRelationshipsAllOfAccessPointsInner()  # noqa: E501
        if include_optional:
            return ControllerAllOfRelationshipsAllOfAccessPointsInner(
                id = 'MTk5NzYyMjM1MDE1MTY4MjYwLDE5OTc2MjQ4MzgzMjQ4NzY4Mw',
                type = 'device',
                attributes = layer8_auvik_api_client.models.controller_all_of_relationships_all_of_access_points_inner_attributes.controller_allOf_relationships_allOf_accessPoints_inner_attributes(
                    device_name = 'Some Access Point', ),
                links = layer8_auvik_api_client.models.controller_all_of_relationships_all_of_access_points_inner_links.controller_allOf_relationships_allOf_accessPoints_inner_links(
                    self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/device/details/extended/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', 
                    info = 'https://auvikapi.us1.my.auvik.com/v1/inventory/device/info/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', )
            )
        else:
            return ControllerAllOfRelationshipsAllOfAccessPointsInner(
        )
        """

    def testControllerAllOfRelationshipsAllOfAccessPointsInner(self):
        """Test ControllerAllOfRelationshipsAllOfAccessPointsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
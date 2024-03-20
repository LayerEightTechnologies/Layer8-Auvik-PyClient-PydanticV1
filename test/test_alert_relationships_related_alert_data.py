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

from layer8_auvik_api_client.models.alert_relationships_related_alert_data import AlertRelationshipsRelatedAlertData  # noqa: E501

class TestAlertRelationshipsRelatedAlertData(unittest.TestCase):
    """AlertRelationshipsRelatedAlertData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertRelationshipsRelatedAlertData:
        """Test AlertRelationshipsRelatedAlertData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertRelationshipsRelatedAlertData`
        """
        model = AlertRelationshipsRelatedAlertData()  # noqa: E501
        if include_optional:
            return AlertRelationshipsRelatedAlertData(
                type = 'alert',
                id = 'MTg2OTI2NTY1MDQ3MDExMDc0LDE5Nzc2OTU1ODM1MTAyMTMxOA',
                attributes = layer8_auvik_api_client.models.alert_relationships_related_alert_data_attributes.alertRelationships_relatedAlert_data_attributes(
                    name = 'High Storage Utilization Cleared', ),
                links = layer8_auvik_api_client.models.alert_relationships_related_alert_data_links.alertRelationships_relatedAlert_data_links(
                    dashboard = 'https://sampledomain.my.auvik.com/#entity/root/alerts/details/alert/382919292406038807', 
                    self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/interface/info/MTk5NTAyNzg2ODc3MDYzNjgxLDE5OTUwMzc3Nzk1Njg4ODgzNQ', )
            )
        else:
            return AlertRelationshipsRelatedAlertData(
        )
        """

    def testAlertRelationshipsRelatedAlertData(self):
        """Test AlertRelationshipsRelatedAlertData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

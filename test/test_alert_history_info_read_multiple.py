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

from layer8_auvik_api_client.models.alert_history_info_read_multiple import AlertHistoryInfoReadMultiple  # noqa: E501

class TestAlertHistoryInfoReadMultiple(unittest.TestCase):
    """AlertHistoryInfoReadMultiple unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertHistoryInfoReadMultiple:
        """Test AlertHistoryInfoReadMultiple
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertHistoryInfoReadMultiple`
        """
        model = AlertHistoryInfoReadMultiple()  # noqa: E501
        if include_optional:
            return AlertHistoryInfoReadMultiple(
                data = [
                    layer8_auvik_api_client.models.alerts_resource_object.alertsResourceObject(
                        type = 'alert', 
                        id = 'MTg2OTI2NTY1MDQ3MDExMDc0LDE5Nzc2OTU1ODM1MTAyMTMxOA', 
                        attributes = layer8_auvik_api_client.models.alert_attributes.alertAttributes(
                            name = 'Printer - Low Ink Level', 
                            severity = 'warning', 
                            status = 'created', 
                            alert_definition_id = 'MTUyOTA0ODIyMzg5ODgwOTMwLDAsMTIzNAo', 
                            specification_id = '-400', 
                            detected_on = '2018-11-22T22:07:18.407Z', 
                            description = 'This printer is reporting an ink percentage of 20% for black ink', 
                            dismissed = True, 
                            dispatched = True, 
                            external_ticket = [
                                layer8_auvik_api_client.models.alert_attributes_external_ticket.alertAttributes_externalTicket(
                                    id = '56003', 
                                    system = 'Connectwise_Cloud', )
                                ], ), 
                        links = layer8_auvik_api_client.models.alerts_resource_object_links.alertsResourceObject_links(
                            dashboard = 'https://sampledomain.my.auvik.com/#entity/root/alerts/details/alert/382919292406038807', 
                            self = 'https://auvikapi.us1.my.auvik.com/v1/alert/history/info/MTk5NTAyNzg2ODc3MDYzMTY5LDE5OTUwMjc5MTExMjc4NTkyMw', ), 
                        relationships = layer8_auvik_api_client.models.alert_relationships.alertRelationships(
                            tenant = layer8_auvik_api_client.models.tenant.tenant(
                                data = layer8_auvik_api_client.models.tenant_data.tenant_data(
                                    type = 'tenant', 
                                    id = '195798545063742726', ), ), 
                            related_alert = layer8_auvik_api_client.models.alert_relationships_related_alert.alertRelationships_relatedAlert(), 
                            entity = layer8_auvik_api_client.models.alert_relationships_entity.alertRelationships_entity(), ), )
                    ],
                links = layer8_auvik_api_client.models.alert_history_info_read_multiple_links.alertHistoryInfoReadMultiple_links(
                    next = 'https://auvikapi.us1.my.auvik.com/v1/alert/history/info?page[after]=Y3Vyc29yOk16TXpPVE0wT0RRNU1UQTROemN4TlRneExETXpNemt6TkRnME56QXpORFF5TmpFeU5R&page[first]=300', 
                    prev = 'https://auvikapi.us1.my.auvik.com/v1/alert/history/info?page[before]=Y3Vyc29yOk16TXpPVE0wT0RRNU1UQTROemN4TlRneExETXpNemt6TkRnME56QXpORFF5TmpFeU5R&page[last]=300', 
                    first = 'https://auvikapi.us1.my.auvik.com/v1/alert/history/info?page[first]=300', 
                    last = 'https://auvikapi.us1.my.auvik.com/v1/alert/history/info?page[last]=300', ),
                meta = layer8_auvik_api_client.models.meta_object.meta object(
                    total_pages = 5, )
            )
        else:
            return AlertHistoryInfoReadMultiple(
        )
        """

    def testAlertHistoryInfoReadMultiple(self):
        """Test AlertHistoryInfoReadMultiple"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
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

from layer8_auvik_api_client.models.device_usage_relationships import DeviceUsageRelationships  # noqa: E501

class TestDeviceUsageRelationships(unittest.TestCase):
    """DeviceUsageRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceUsageRelationships:
        """Test DeviceUsageRelationships
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceUsageRelationships`
        """
        model = DeviceUsageRelationships()  # noqa: E501
        if include_optional:
            return DeviceUsageRelationships(
                client = layer8_auvik_api_client.models.device_usage_relationships_client.deviceUsageRelationships_client(
                    data = layer8_auvik_api_client.models.device_usage_relationships_client_data.deviceUsageRelationships_client_data(
                        id = '199762235015168004', 
                        type = 'clientUsage', 
                        attributes = layer8_auvik_api_client.models.device_usage_relationships_client_data_attributes.deviceUsageRelationships_client_data_attributes(
                            domain_prefix = 'mspclient', ), 
                        links = layer8_auvik_api_client.models.client_usage_resource_object_links.clientUsageResourceObject_links(
                            dashboard = 'https://sampledomain.my.auvik.com/#admin/settings/billingUsage', 
                            tenant_record = 'https://auvikapi.us1.my.auvik.com/v1/tenants/detail/199762235015168516?tenantDomainPrefix=sampledomain', 
                            self = 'https://auvikapi.us1.my.auvik.com/v1/billing/usage/client?tenants=199762235015168516&from=2019-06-01&to=2019-06-30', ), ), )
            )
        else:
            return DeviceUsageRelationships(
        )
        """

    def testDeviceUsageRelationships(self):
        """Test DeviceUsageRelationships"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

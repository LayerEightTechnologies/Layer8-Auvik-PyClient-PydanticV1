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

from layer8_auvik_api_client.models.endpoint_stats import EndpointStats  # noqa: E501

class TestEndpointStats(unittest.TestCase):
    """EndpointStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointStats:
        """Test EndpointStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointStats`
        """
        model = EndpointStats()  # noqa: E501
        if include_optional:
            return EndpointStats(
                id = 'NzkyMyw1NTcxNjU0Njc2MTQwODY4MTI',
                ip_address = '192.0.2.10',
                stats = [
                    layer8_auvik_api_client.models.stat_item.statItem(
                        name = 'Statistic name', 
                        index = '1', 
                        legend = [
                            'Statistic value'
                            ], 
                        unit = [
                            'percent'
                            ], 
                        data = [
                            [
                                1.337
                                ]
                            ], )
                    ]
            )
        else:
            return EndpointStats(
        )
        """

    def testEndpointStats(self):
        """Test EndpointStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

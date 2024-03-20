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

from layer8_auvik_api_client.models.device_availability_statistics_read import DeviceAvailabilityStatisticsRead  # noqa: E501

class TestDeviceAvailabilityStatisticsRead(unittest.TestCase):
    """DeviceAvailabilityStatisticsRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceAvailabilityStatisticsRead:
        """Test DeviceAvailabilityStatisticsRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceAvailabilityStatisticsRead`
        """
        model = DeviceAvailabilityStatisticsRead()  # noqa: E501
        if include_optional:
            return DeviceAvailabilityStatisticsRead(
                data = layer8_auvik_api_client.models.device_availability_statistics_resource_object.deviceAvailabilityStatisticsResourceObject(
                    id = 'NzkyMywxOTgzNTA5OTc0NDM3MTU4NDQsc3RhdC9kZXZpY2UvYmFuZHdpZHRoOmhvdXI', 
                    type = 'deviceAvailabilityStatistics', 
                    attributes = layer8_auvik_api_client.models.statistics_attributes.statisticsAttributes(
                        report_period = layer8_auvik_api_client.models.report_period.reportPeriod(
                            from_time = '2020-02-18T00:00:00.000Z', 
                            thru_time = '2020-02-19T00:00:00.000Z', ), 
                        interval = 'hour', 
                        stat_type = 'statTypeName', 
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
                            ], ), 
                    relationships = layer8_auvik_api_client.models.device_statistics_relationships.deviceStatisticsRelationships(
                        device = layer8_auvik_api_client.models.device_statistics_relationships_device.deviceStatisticsRelationships_device(), 
                        tenant = layer8_auvik_api_client.models.tenant.tenant(), ), 
                    links = layer8_auvik_api_client.models.device_statistics_resource_object_links.deviceStatisticsResourceObject_links(
                        dashboard = 'https://auvikapi.us1.my.auvik.com/v1/inventory/device/info/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', 
                        self = 'https://auvikapi.us1.my.auvik.com/v1/stat/device/bandwidth/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw?from=2019-06-01&to=2019-06-30', ), )
            )
        else:
            return DeviceAvailabilityStatisticsRead(
        )
        """

    def testDeviceAvailabilityStatisticsRead(self):
        """Test DeviceAvailabilityStatisticsRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
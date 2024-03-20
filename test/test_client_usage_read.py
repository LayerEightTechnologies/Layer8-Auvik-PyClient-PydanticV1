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

from layer8_auvik_api_client.models.client_usage_read import ClientUsageRead  # noqa: E501

class TestClientUsageRead(unittest.TestCase):
    """ClientUsageRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientUsageRead:
        """Test ClientUsageRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientUsageRead`
        """
        model = ClientUsageRead()  # noqa: E501
        if include_optional:
            return ClientUsageRead(
                data = [
                    layer8_auvik_api_client.models.client_usage_resource_object.clientUsageResourceObject(
                        id = '199762235015168516', 
                        type = 'clientUsage', 
                        attributes = layer8_auvik_api_client.models.client_usage_attributes.clientUsageAttributes(
                            domain_prefix = 'sampledomain', 
                            billable_days = 30, 
                            usage_period = layer8_auvik_api_client.models.client_usage_attributes_usage_period.clientUsageAttributes_usagePeriod(
                                start_date = '2019-06-01T00:00:00Z', 
                                end_date = '2019-07-01T00:00:00Z', 
                                length_in_days = 30, ), 
                            device_usage = layer8_auvik_api_client.models.client_usage_attributes_device_usage.clientUsageAttributes_deviceUsage(
                                total_days = 150, 
                                average_days = 5, 
                                total_days_by_client_type = layer8_auvik_api_client.models.client_usage_attributes_device_usage_total_days_by_client_type.clientUsageAttributes_deviceUsage_totalDaysByClientType(
                                    notier = 0, 
                                    light = 30, 
                                    essentials = 30, 
                                    performance = 120, ), 
                                average_days_by_client_type = layer8_auvik_api_client.models.client_usage_attributes_device_usage_average_days_by_client_type.clientUsageAttributes_deviceUsage_averageDaysByClientType(
                                    notier = 0, 
                                    light = 1, 
                                    essentials = 1, 
                                    performance = 4, ), ), 
                            client_usage = layer8_auvik_api_client.models.client_usage_attributes_client_usage.clientUsageAttributes_clientUsage(
                                total_days = 150, 
                                averaged_days = 5, ), ), 
                        relationships = layer8_auvik_api_client.models.client_usage_relationships.clientUsageRelationships(
                            devices = layer8_auvik_api_client.models.client_usage_relationships_devices.clientUsageRelationships_devices(
                                data = [
                                    layer8_auvik_api_client.models.client_usage_relationships_devices_data.clientUsageRelationships_devices_data(
                                        id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', 
                                        type = 'deviceUsage', 
                                        links = layer8_auvik_api_client.models.client_usage_relationships_devices_links.clientUsageRelationships_devices_links(
                                            device_record = 'https://auvikapi.us1.my.auvik.com/v1/inventory/device/info/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', 
                                            self = 'https://auvikapi.us1.my.auvik.com/v1/billing/usage/device/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw?from=2019-06-01&to=2019-06-30', ), )
                                    ], ), 
                            clients = layer8_auvik_api_client.models.client_usage_relationships_clients.clientUsageRelationships_clients(), ), 
                        links = layer8_auvik_api_client.models.client_usage_resource_object_links.clientUsageResourceObject_links(
                            dashboard = 'https://sampledomain.my.auvik.com/#admin/settings/billingUsage', 
                            tenant_record = 'https://auvikapi.us1.my.auvik.com/v1/tenants/detail/199762235015168516?tenantDomainPrefix=sampledomain', 
                            self = 'https://auvikapi.us1.my.auvik.com/v1/billing/usage/client?tenants=199762235015168516&from=2019-06-01&to=2019-06-30', ), )
                    ]
            )
        else:
            return ClientUsageRead(
        )
        """

    def testClientUsageRead(self):
        """Test ClientUsageRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

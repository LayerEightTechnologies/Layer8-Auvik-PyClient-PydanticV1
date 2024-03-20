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

from layer8_auvik_api_client.models.network_info_read_multiple import NetworkInfoReadMultiple  # noqa: E501

class TestNetworkInfoReadMultiple(unittest.TestCase):
    """NetworkInfoReadMultiple unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkInfoReadMultiple:
        """Test NetworkInfoReadMultiple
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkInfoReadMultiple`
        """
        model = NetworkInfoReadMultiple()  # noqa: E501
        if include_optional:
            return NetworkInfoReadMultiple(
                data = [
                    layer8_auvik_api_client.models.networks_resource_object.networksResourceObject(
                        type = 'network', 
                        id = 'MTk5NTAyNzg2ODc3MDYzMTY5LDE5OTUwMjc5MTExMjc4NTkyMw', 
                        attributes = layer8_auvik_api_client.models.network_attributes.networkAttributes(
                            network_type = 'routed', 
                            network_name = '192.168.4.0/24', 
                            description = '192.168.4.0/24', 
                            scan_status = 'true', 
                            last_modified = '2018-03-12T12:00:00.000Z', ), 
                        relationships = layer8_auvik_api_client.models.network_relationships.networkRelationships(
                            network_detail = layer8_auvik_api_client.models.network_relationships_network_detail.networkRelationships_networkDetail(
                                data = layer8_auvik_api_client.models.network_relationships_network_detail_data.networkRelationships_networkDetail_data(
                                    type = 'networkDetail', 
                                    id = 'MTk5NTAyNzg2ODc3MDYzMTY5LDE5OTUwMjc5MTExMjc4NTkyMw', 
                                    links = layer8_auvik_api_client.models.network_relationships_network_detail_data_links.networkRelationships_networkDetail_data_links(
                                        self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/network/detail/MTk5NTAyNzg2ODc3MDYzMTY5LDE5OTUwMjc5MTExMjc4NTkyMw', 
                                        dashboard = 'https://sampledomain.my.auvik.com/#entity/network/199502791112896003/dashboard', ), ), ), 
                            tenant = layer8_auvik_api_client.models.tenant.tenant(), 
                            devices = layer8_auvik_api_client.models.network_relationships_devices.networkRelationships_devices(), ), 
                        links = layer8_auvik_api_client.models.networks_resource_object_links.networksResourceObject_links(
                            dashboard = 'https://sampledomain.my.auvik.com/#entity/network/199502791112896003/dashboard', 
                            self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/network/info/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', ), )
                    ],
                included = [
                    layer8_auvik_api_client.models.network_details_resource_object.networkDetailsResourceObject(
                        type = 'networkDetail', 
                        id = 'MTk5NTAyNzg2ODc3MDYzMTY5LDE5OTUwMjc5MTExMjc4NTkyMw', 
                        attributes = layer8_auvik_api_client.models.network_details_attributes.networkDetailsAttributes(
                            scope = 'private', 
                            primary_collector = '98a1790e-ec59-481f-8529-4f836b0bd1ca', 
                            secondary_collectors = [
                                '8e604713-7606-4e8c-8200-bd6d4317e069'
                                ], 
                            collector_selection = 'automatic', 
                            excluded_ip_addresses = [
                                '192.168.4.10-192.168.4.25'
                                ], ), 
                        relationships = layer8_auvik_api_client.models.network_details_relationships.networkDetailsRelationships(
                            tenant = layer8_auvik_api_client.models.tenant.tenant(
                                data = layer8_auvik_api_client.models.tenant_data.tenant_data(
                                    type = 'tenant', 
                                    id = '195798545063742726', ), ), ), 
                        links = layer8_auvik_api_client.models.network_details_resource_object_links.networkDetailsResourceObject_links(
                            dashboard = 'https://sampledomain.my.auvik.com/#entity/network/199502791112785923/dashboard', 
                            self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/network/detail/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', ), )
                    ],
                links = layer8_auvik_api_client.models.network_info_read_multiple_links.networkInfoReadMultiple_links(
                    next = 'https://auvikapi.us1.my.auvik.com/v1/inventory/network/info?page[after]=Y3Vyc29yOk16TXpPVE0wT0RRNU1UQTROemN4TlRneExETXpNemt6TkRnME56QXpORFF5TmpFeU5R&page[first]=300', 
                    prev = 'https://auvikapi.us1.my.auvik.com/v1/inventory/network/info?page[before]=Y3Vyc29yOk16TXpPVE0wT0RRNU1UQTROemN4TlRneExETXpNemt6TkRnME56QXpORFF5TmpFeU5R&page[last]=300', 
                    first = 'https://auvikapi.us1.my.auvik.com/v1/inventory/network/info?page[first]=300', 
                    last = 'https://auvikapi.us1.my.auvik.com/v1/inventory/network/info?page[last]=300', ),
                meta = layer8_auvik_api_client.models.meta_object.meta object(
                    total_pages = 5, )
            )
        else:
            return NetworkInfoReadMultiple(
        )
        """

    def testNetworkInfoReadMultiple(self):
        """Test NetworkInfoReadMultiple"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
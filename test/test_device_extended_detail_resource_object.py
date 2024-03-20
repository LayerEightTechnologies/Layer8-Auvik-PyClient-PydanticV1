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

from layer8_auvik_api_client.models.device_extended_detail_resource_object import DeviceExtendedDetailResourceObject  # noqa: E501

class TestDeviceExtendedDetailResourceObject(unittest.TestCase):
    """DeviceExtendedDetailResourceObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceExtendedDetailResourceObject:
        """Test DeviceExtendedDetailResourceObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceExtendedDetailResourceObject`
        """
        model = DeviceExtendedDetailResourceObject()  # noqa: E501
        if include_optional:
            return DeviceExtendedDetailResourceObject(
                type = 'deviceExtendedDetail',
                id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw',
                links = layer8_auvik_api_client.models.device_extended_details_device_links.deviceExtendedDetailsDevice_links(
                    self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/device/details/extended/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', 
                    info = 'https://auvikapi.us1.my.auvik.com/v1/inventory/device/info/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', ),
                attributes = None,
                relationships = layer8_auvik_api_client.models.device_relationships.deviceRelationships(
                    tenant = layer8_auvik_api_client.models.tenant.tenant(
                        data = layer8_auvik_api_client.models.tenant_data.tenant_data(
                            type = 'tenant', 
                            id = '195798545063742726', 
                            attributes = layer8_auvik_api_client.models.tenant_data_attributes.tenant_data_attributes(
                                domain_prefix = 'sampledomain', ), ), ), 
                    networks = layer8_auvik_api_client.models.device_relationships_networks.deviceRelationships_networks(), 
                    device_detail = layer8_auvik_api_client.models.device_relationships_device_detail.deviceRelationships_deviceDetail(), )
            )
        else:
            return DeviceExtendedDetailResourceObject(
        )
        """

    def testDeviceExtendedDetailResourceObject(self):
        """Test DeviceExtendedDetailResourceObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from layer8_auvik_api_client.models.config_resource_object import ConfigResourceObject  # noqa: E501

class TestConfigResourceObject(unittest.TestCase):
    """ConfigResourceObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigResourceObject:
        """Test ConfigResourceObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigResourceObject`
        """
        model = ConfigResourceObject()  # noqa: E501
        if include_optional:
            return ConfigResourceObject(
                type = 'configuration',
                id = 'MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw',
                attributes = layer8_auvik_api_client.models.config_attributes.configAttributes(
                    backup_time = '2018-03-12T12:00:00.000Z', 
                    is_running = True, ),
                relationships = layer8_auvik_api_client.models.config_relationships.configRelationships(
                    tenant = layer8_auvik_api_client.models.tenant.tenant(
                        data = layer8_auvik_api_client.models.tenant_data.tenant_data(
                            type = 'tenant', 
                            id = '195798545063742726', 
                            attributes = layer8_auvik_api_client.models.tenant_data_attributes.tenant_data_attributes(
                                domain_prefix = 'sampledomain', ), ), ), 
                    device = layer8_auvik_api_client.models.device_lifecycle_relationships_device.deviceLifecycleRelationships_device(), ),
                links = layer8_auvik_api_client.models.config_resource_object_links.configResourceObject_links(
                    dashboard = 'https://sampledomain.my.auvik.com/#entity/device/199502791113028867/configurations', 
                    self = 'https://auvikapi.us1.my.auvik.com/v1/inventory/configuration/MTk5NTAyNzg2ODc3MDYzNDI1LDE5OTUwMjc5MTExMzAyODg2Nw', )
            )
        else:
            return ConfigResourceObject(
        )
        """

    def testConfigResourceObject(self):
        """Test ConfigResourceObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

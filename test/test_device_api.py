# coding: utf-8

"""
    Auvik API

    To use the Auvik APIs, you’ll need a <a href=\"https://support.auvik.com/hc/en-us/articles/204309114-#topic_generate\" target=\"_blank\">valid Auvik user and the user’s API key</a>. The user must also have the correct <a href=\" https://support.auvik.com/hc/en-us/articles/115002815966\" target=\"_blank\">role permissions</a>.<br>     <br>     Note: The word <i>tenant</i> as it appears in the API descriptions means one of Auvik’s supported tenant types: multi-client or client.<br><br>All date formats are formatted in the format of YYYY-MM-DDTHH:MM:SS.sssZ, as describe in ISO 8061<br><br>To find out more about Auvik’s APIs, <a href=\"https://support.auvik.com/hc/en-us/articles/360017965092\" target=\"_blank\">click here.</a>

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from layer8_auvik_api_client.api.device_api import DeviceApi  # noqa: E501


class TestDeviceApi(unittest.TestCase):
    """DeviceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DeviceApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_read_multiple_device_details(self) -> None:
        """Test case for read_multiple_device_details

        Read Multiple Devices’ Details  # noqa: E501
        """
        pass

    def test_read_multiple_device_extended_detail(self) -> None:
        """Test case for read_multiple_device_extended_detail

        Read Multiple Devices’ Extended Details  # noqa: E501
        """
        pass

    def test_read_multiple_device_info(self) -> None:
        """Test case for read_multiple_device_info

        Read Multiple Devices’ Info  # noqa: E501
        """
        pass

    def test_read_multiple_device_lifecycle(self) -> None:
        """Test case for read_multiple_device_lifecycle

        Read Multiple Devices’ Lifecycle Info  # noqa: E501
        """
        pass

    def test_read_multiple_device_warranty(self) -> None:
        """Test case for read_multiple_device_warranty

        Read Multiple Devices’ Warranty Info  # noqa: E501
        """
        pass

    def test_read_single_device_details(self) -> None:
        """Test case for read_single_device_details

        Read a Single Device’s Details  # noqa: E501
        """
        pass

    def test_read_single_device_extended_detail(self) -> None:
        """Test case for read_single_device_extended_detail

        Read a Single Device’s Extended Details  # noqa: E501
        """
        pass

    def test_read_single_device_info(self) -> None:
        """Test case for read_single_device_info

        Read a Single Device’s Info  # noqa: E501
        """
        pass

    def test_read_single_device_lifecycle(self) -> None:
        """Test case for read_single_device_lifecycle

        Read a Single Device’s Lifecycle Info  # noqa: E501
        """
        pass

    def test_read_single_device_warranty(self) -> None:
        """Test case for read_single_device_warranty

        Read a Single Device’s Warranty Info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
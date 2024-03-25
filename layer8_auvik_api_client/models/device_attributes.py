# coding: utf-8

"""
Auvik API

To use the Auvik APIs, you’ll need a <a href=\"https://support.auvik.com/hc/en-us/articles/204309114-#topic_generate\" target=\"_blank\">valid Auvik user and the user’s API key</a>. The user must also have the correct <a href=\" https://support.auvik.com/hc/en-us/articles/115002815966\" target=\"_blank\">role permissions</a>.<br>     <br>     Note: The word <i>tenant</i> as it appears in the API descriptions means one of Auvik’s supported tenant types: multi-client or client.<br><br>All date formats are formatted in the format of YYYY-MM-DDTHH:MM:SS.sssZ, as describe in ISO 8061<br><br>To find out more about Auvik’s APIs, <a href=\"https://support.auvik.com/hc/en-us/articles/360017965092\" target=\"_blank\">click here.</a>

The version of the OpenAPI document: v1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator


class DeviceAttributes(BaseModel):
    """
    The type-specific properties of the devices object returned  # noqa: E501
    """

    ip_addresses: conlist(StrictStr) = Field(
        ..., alias="ipAddresses", description="Device's local IP addresses"
    )
    device_name: StrictStr = Field(..., alias="deviceName", description="Device's name")
    device_type: StrictStr = Field(
        ..., alias="deviceType", description="What type of device it is"
    )
    make_model: Optional[StrictStr] = Field(
        ..., alias="makeModel", description="Make and model of this device"
    )
    vendor_name: Optional[StrictStr] = Field(
        ..., alias="vendorName", description="Vendor name for this device"
    )
    software_version: Optional[StrictStr] = Field(
        ..., alias="softwareVersion", description="Devices software version, if known"
    )
    serial_number: Optional[StrictStr] = Field(
        ..., alias="serialNumber", description="Device's serial number"
    )
    description: StrictStr = Field(..., description="Description")
    firmware_version: Optional[StrictStr] = Field(
        ..., alias="firmwareVersion", description="Device's firmware version"
    )
    last_modified: StrictStr = Field(
        ...,
        alias="lastModified",
        description="When one of this device's attributes was last modified",
    )
    last_seen_time: Optional[StrictStr] = Field(
        None, alias="lastSeenTime", description="Last seen online date/time of a device"
    )
    online_status: StrictStr = Field(
        ..., alias="onlineStatus", description="Device's online status"
    )
    __properties = [
        "ipAddresses",
        "deviceName",
        "deviceType",
        "makeModel",
        "vendorName",
        "softwareVersion",
        "serialNumber",
        "description",
        "firmwareVersion",
        "lastModified",
        "lastSeenTime",
        "onlineStatus",
    ]

    @validator("device_type")
    def device_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (
            "unknown",
            "switch",
            "l3Switch",
            "router",
            "accessPoint",
            "firewall",
            "workstation",
            "server",
            "storage",
            "printer",
            "copier",
            "hypervisor",
            "multimedia",
            "phone",
            "tablet",
            "handheld",
            "virtualAppliance",
            "bridge",
            "controller",
            "hub",
            "modem",
            "ups",
            "module",
            "loadBalancer",
            "camera",
            "telecommunications",
            "packetProcessor",
            "chassis",
            "airConditioner",
            "virtualMachine",
            "pdu",
            "ipPhone",
            "backhaul",
            "internetOfThings",
            "voipSwitch",
            "stack",
            "backupDevice",
            "timeClock",
            "lightingDevice",
            "audioVisual",
            "securityAppliance",
            "utm",
            "alarm",
            "buildingManagement",
            "ipmi",
            "thinAccessPoint",
            "thinClient",
        ):
            raise ValueError(
                "must be one of enum values ('unknown', 'switch', 'l3Switch', 'router', 'accessPoint', 'firewall', 'workstation', 'server', 'storage', 'printer', 'copier', 'hypervisor', 'multimedia', 'phone', 'tablet', 'handheld', 'virtualAppliance', 'bridge', 'controller', 'hub', 'modem', 'ups', 'module', 'loadBalancer', 'camera', 'telecommunications', 'packetProcessor', 'chassis', 'airConditioner', 'virtualMachine', 'pdu', 'ipPhone', 'backhaul', 'internetOfThings', 'voipSwitch', 'stack', 'backupDevice', 'timeClock', 'lightingDevice', 'audioVisual', 'securityAppliance', 'utm', 'alarm', 'buildingManagement', 'ipmi', 'thinAccessPoint', 'thinClient')"
            )
        return value

    @validator("online_status")
    def online_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (
            "online",
            "offline",
            "unreachable",
            "testing",
            "unknown",
            "dormant",
            "notPresent",
            "lowerLayerDown",
        ):
            raise ValueError(
                "must be one of enum values ('online', 'offline', 'unreachable', 'testing', 'unknown', 'dormant', 'notPresent', 'lowerLayerDown')"
            )
        return value

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DeviceAttributes:
        """Create an instance of DeviceAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if make_model (nullable) is None
        # and __fields_set__ contains the field
        if self.make_model is None and "make_model" in self.__fields_set__:
            _dict["makeModel"] = None

        # set to None if vendor_name (nullable) is None
        # and __fields_set__ contains the field
        if self.vendor_name is None and "vendor_name" in self.__fields_set__:
            _dict["vendorName"] = None

        # set to None if software_version (nullable) is None
        # and __fields_set__ contains the field
        if self.software_version is None and "software_version" in self.__fields_set__:
            _dict["softwareVersion"] = None

        # set to None if serial_number (nullable) is None
        # and __fields_set__ contains the field
        if self.serial_number is None and "serial_number" in self.__fields_set__:
            _dict["serialNumber"] = None

        # set to None if firmware_version (nullable) is None
        # and __fields_set__ contains the field
        if self.firmware_version is None and "firmware_version" in self.__fields_set__:
            _dict["firmwareVersion"] = None

        # set to None if last_seen_time (nullable) is None
        # and __fields_set__ contains the field
        if self.last_seen_time is None and "last_seen_time" in self.__fields_set__:
            _dict["lastSeenTime"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeviceAttributes:
        """Create an instance of DeviceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeviceAttributes.parse_obj(obj)

        _obj = DeviceAttributes.parse_obj(
            {
                "ip_addresses": obj.get("ipAddresses"),
                "device_name": obj.get("deviceName"),
                "device_type": obj.get("deviceType"),
                "make_model": obj.get("makeModel"),
                "vendor_name": obj.get("vendorName"),
                "software_version": obj.get("softwareVersion"),
                "serial_number": obj.get("serialNumber"),
                "description": obj.get("description"),
                "firmware_version": obj.get("firmwareVersion"),
                "last_modified": obj.get("lastModified"),
                "last_seen_time": obj.get("lastSeenTime"),
                "online_status": obj.get("onlineStatus"),
            }
        )
        return _obj

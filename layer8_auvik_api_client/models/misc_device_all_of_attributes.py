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
from layer8_auvik_api_client.models.misc_device_all_of_attributes_all_of_tunnels_inner import MiscDeviceAllOfAttributesAllOfTunnelsInner

class MiscDeviceAllOfAttributes(BaseModel):
    """
    MiscDeviceAllOfAttributes
    """
    device_name: StrictStr = Field(..., alias="deviceName", description="Device's name")
    last_modified: Optional[StrictStr] = Field(None, alias="lastModified", description="When one of this device's attributes was last modified")
    last_seen_time: Optional[StrictStr] = Field(None, alias="lastSeenTime", description="Last seen online date/time of a device")
    device_type: StrictStr = Field(..., alias="deviceType", description="What type of device it is")
    tunnels: conlist(MiscDeviceAllOfAttributesAllOfTunnelsInner) = Field(..., description="List of tunnels on the device")
    __properties = ["deviceName", "lastModified", "lastSeenTime", "deviceType", "tunnels"]

    @validator('device_type')
    def device_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('unknown', 'switch', 'l3Switch', 'router', 'firewall', 'workstation', 'server', 'storage', 'printer', 'copier', 'multimedia', 'phone', 'tablet', 'handheld', 'virtualAppliance', 'bridge', 'hub', 'modem', 'ups', 'inferredSwitch', 'module', 'loadBalancer', 'camera', 'telecommunications', 'packetProcessor', 'chassis', 'airConditioner', 'inferredHub', 'pdu', 'ipPhone', 'backhaul', 'internetOfThings', 'voipSwitch', 'backupDevice', 'timeClock', 'lightingDevice', 'audioVisual', 'securityAppliance', 'utm', 'alarm', 'buildingManagement', 'ipmi', 'thinAccessPoint', 'thinClient'):
            raise ValueError("must be one of enum values ('unknown', 'switch', 'l3Switch', 'router', 'firewall', 'workstation', 'server', 'storage', 'printer', 'copier', 'multimedia', 'phone', 'tablet', 'handheld', 'virtualAppliance', 'bridge', 'hub', 'modem', 'ups', 'inferredSwitch', 'module', 'loadBalancer', 'camera', 'telecommunications', 'packetProcessor', 'chassis', 'airConditioner', 'inferredHub', 'pdu', 'ipPhone', 'backhaul', 'internetOfThings', 'voipSwitch', 'backupDevice', 'timeClock', 'lightingDevice', 'audioVisual', 'securityAppliance', 'utm', 'alarm', 'buildingManagement', 'ipmi', 'thinAccessPoint', 'thinClient')")
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
    def from_json(cls, json_str: str) -> MiscDeviceAllOfAttributes:
        """Create an instance of MiscDeviceAllOfAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tunnels (list)
        _items = []
        if self.tunnels:
            for _item in self.tunnels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tunnels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MiscDeviceAllOfAttributes:
        """Create an instance of MiscDeviceAllOfAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MiscDeviceAllOfAttributes.parse_obj(obj)

        _obj = MiscDeviceAllOfAttributes.parse_obj({
            "device_name": obj.get("deviceName"),
            "last_modified": obj.get("lastModified"),
            "last_seen_time": obj.get("lastSeenTime"),
            "device_type": obj.get("deviceType"),
            "tunnels": [MiscDeviceAllOfAttributesAllOfTunnelsInner.from_dict(_item) for _item in obj.get("tunnels")] if obj.get("tunnels") is not None else None
        })
        return _obj


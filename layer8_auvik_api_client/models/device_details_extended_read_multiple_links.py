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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class DeviceDetailsExtendedReadMultipleLinks(BaseModel):
    """
    Pagination related links  # noqa: E501
    """
    next: Optional[StrictStr] = Field(None, description="Next page in the data set")
    prev: Optional[StrictStr] = Field(None, description="Previous page in the data set")
    first: Optional[StrictStr] = Field(None, description="First page in the data set")
    last: Optional[StrictStr] = Field(None, description="Last page in the data set")
    __properties = ["next", "prev", "first", "last"]

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
    def from_json(cls, json_str: str) -> DeviceDetailsExtendedReadMultipleLinks:
        """Create an instance of DeviceDetailsExtendedReadMultipleLinks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeviceDetailsExtendedReadMultipleLinks:
        """Create an instance of DeviceDetailsExtendedReadMultipleLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeviceDetailsExtendedReadMultipleLinks.parse_obj(obj)

        _obj = DeviceDetailsExtendedReadMultipleLinks.parse_obj({
            "next": obj.get("next"),
            "prev": obj.get("prev"),
            "first": obj.get("first"),
            "last": obj.get("last")
        })
        return _obj



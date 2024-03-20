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
from pydantic import BaseModel, Field, StrictStr, conlist
from layer8_auvik_api_client.models.stat_item2_data_inner_inner import StatItem2DataInnerInner

class StatItem2(BaseModel):
    """
    StatItem2
    """
    legend: Optional[conlist(StrictStr)] = Field(None, description="A description of the stats data columns")
    data: Optional[conlist(conlist(StatItem2DataInnerInner))] = Field(None, description="A list of rows of historical values, as described by the legend")
    __properties = ["legend", "data"]

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
    def from_json(cls, json_str: str) -> StatItem2:
        """Create an instance of StatItem2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list of list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item if _inner_item is not None]
                    )
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StatItem2:
        """Create an instance of StatItem2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StatItem2.parse_obj(obj)

        _obj = StatItem2.parse_obj({
            "legend": obj.get("legend"),
            "data": [
                    [StatItem2DataInnerInner.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj.get("data")
                ] if obj.get("data") is not None else None
        })
        return _obj



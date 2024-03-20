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
from layer8_auvik_api_client.models.report_period import ReportPeriod
from layer8_auvik_api_client.models.stat_item import StatItem

class StatisticsAttributes(BaseModel):
    """
    The type-specific properties of the statistics object returned  # noqa: E501
    """
    report_period: Optional[ReportPeriod] = Field(None, alias="reportPeriod")
    interval: Optional[StrictStr] = Field(None, description="The reporting interval for the statistics")
    stat_type: Optional[StrictStr] = Field(None, alias="statType", description="The type of statistic that was returned")
    stats: Optional[conlist(StatItem)] = Field(None, description="The list of statistics reported for the entity")
    __properties = ["reportPeriod", "interval", "statType", "stats"]

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
    def from_json(cls, json_str: str) -> StatisticsAttributes:
        """Create an instance of StatisticsAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of report_period
        if self.report_period:
            _dict['reportPeriod'] = self.report_period.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in stats (list)
        _items = []
        if self.stats:
            for _item in self.stats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stats'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StatisticsAttributes:
        """Create an instance of StatisticsAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StatisticsAttributes.parse_obj(obj)

        _obj = StatisticsAttributes.parse_obj({
            "report_period": ReportPeriod.from_dict(obj.get("reportPeriod")) if obj.get("reportPeriod") is not None else None,
            "interval": obj.get("interval"),
            "stat_type": obj.get("statType"),
            "stats": [StatItem.from_dict(_item) for _item in obj.get("stats")] if obj.get("stats") is not None else None
        })
        return _obj



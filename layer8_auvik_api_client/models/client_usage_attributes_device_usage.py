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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from layer8_auvik_api_client.models.client_usage_attributes_device_usage_average_days_by_client_type import ClientUsageAttributesDeviceUsageAverageDaysByClientType
from layer8_auvik_api_client.models.client_usage_attributes_device_usage_total_days_by_client_type import ClientUsageAttributesDeviceUsageTotalDaysByClientType

class ClientUsageAttributesDeviceUsage(BaseModel):
    """
    Roll up of device usage on this client (and its children if a multi-client)  # noqa: E501
    """
    total_days: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalDays", description="The total billable device days for this client and all of its children across the usage period")
    average_days: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="averageDays", description="The average billable device days for this client and all of its children across the usage period")
    total_days_by_client_type: Optional[ClientUsageAttributesDeviceUsageTotalDaysByClientType] = Field(None, alias="totalDaysByClientType")
    average_days_by_client_type: Optional[ClientUsageAttributesDeviceUsageAverageDaysByClientType] = Field(None, alias="averageDaysByClientType")
    __properties = ["totalDays", "averageDays", "totalDaysByClientType", "averageDaysByClientType"]

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
    def from_json(cls, json_str: str) -> ClientUsageAttributesDeviceUsage:
        """Create an instance of ClientUsageAttributesDeviceUsage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of total_days_by_client_type
        if self.total_days_by_client_type:
            _dict['totalDaysByClientType'] = self.total_days_by_client_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of average_days_by_client_type
        if self.average_days_by_client_type:
            _dict['averageDaysByClientType'] = self.average_days_by_client_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClientUsageAttributesDeviceUsage:
        """Create an instance of ClientUsageAttributesDeviceUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClientUsageAttributesDeviceUsage.parse_obj(obj)

        _obj = ClientUsageAttributesDeviceUsage.parse_obj({
            "total_days": obj.get("totalDays"),
            "average_days": obj.get("averageDays"),
            "total_days_by_client_type": ClientUsageAttributesDeviceUsageTotalDaysByClientType.from_dict(obj.get("totalDaysByClientType")) if obj.get("totalDaysByClientType") is not None else None,
            "average_days_by_client_type": ClientUsageAttributesDeviceUsageAverageDaysByClientType.from_dict(obj.get("averageDaysByClientType")) if obj.get("averageDaysByClientType") is not None else None
        })
        return _obj



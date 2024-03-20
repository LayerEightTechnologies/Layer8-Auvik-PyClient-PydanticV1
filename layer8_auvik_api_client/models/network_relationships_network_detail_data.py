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
from pydantic import BaseModel, Field, StrictStr, validator
from layer8_auvik_api_client.models.network_relationships_network_detail_data_links import NetworkRelationshipsNetworkDetailDataLinks

class NetworkRelationshipsNetworkDetailData(BaseModel):
    """
    A network detail object  # noqa: E501
    """
    type: Optional[StrictStr] = Field(None, description="The type of object in the API")
    id: Optional[StrictStr] = Field(None, description="The unique identifier for this network")
    links: Optional[NetworkRelationshipsNetworkDetailDataLinks] = None
    __properties = ["type", "id", "links"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('networkDetail'):
            raise ValueError("must be one of enum values ('networkDetail')")
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
    def from_json(cls, json_str: str) -> NetworkRelationshipsNetworkDetailData:
        """Create an instance of NetworkRelationshipsNetworkDetailData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NetworkRelationshipsNetworkDetailData:
        """Create an instance of NetworkRelationshipsNetworkDetailData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NetworkRelationshipsNetworkDetailData.parse_obj(obj)

        _obj = NetworkRelationshipsNetworkDetailData.parse_obj({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "links": NetworkRelationshipsNetworkDetailDataLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None
        })
        return _obj



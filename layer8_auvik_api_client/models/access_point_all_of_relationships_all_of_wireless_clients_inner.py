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
from layer8_auvik_api_client.models.access_point_all_of_relationships_all_of_wireless_clients_inner_attributes import AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes
from layer8_auvik_api_client.models.controller_all_of_relationships_all_of_access_points_inner_links import ControllerAllOfRelationshipsAllOfAccessPointsInnerLinks

class AccessPointAllOfRelationshipsAllOfWirelessClientsInner(BaseModel):
    """
    AccessPointAllOfRelationshipsAllOfWirelessClientsInner
    """
    id: Optional[StrictStr] = Field(None, description="This wireless client's ID")
    type: Optional[StrictStr] = Field(None, description="Resource type of this wireless client")
    attributes: Optional[AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes] = None
    links: Optional[ControllerAllOfRelationshipsAllOfAccessPointsInnerLinks] = None
    __properties = ["id", "type", "attributes", "links"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('device'):
            raise ValueError("must be one of enum values ('device')")
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
    def from_json(cls, json_str: str) -> AccessPointAllOfRelationshipsAllOfWirelessClientsInner:
        """Create an instance of AccessPointAllOfRelationshipsAllOfWirelessClientsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessPointAllOfRelationshipsAllOfWirelessClientsInner:
        """Create an instance of AccessPointAllOfRelationshipsAllOfWirelessClientsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessPointAllOfRelationshipsAllOfWirelessClientsInner.parse_obj(obj)

        _obj = AccessPointAllOfRelationshipsAllOfWirelessClientsInner.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "attributes": AccessPointAllOfRelationshipsAllOfWirelessClientsInnerAttributes.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None,
            "links": ControllerAllOfRelationshipsAllOfAccessPointsInnerLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None
        })
        return _obj



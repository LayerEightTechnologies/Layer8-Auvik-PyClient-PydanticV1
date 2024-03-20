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
from pydantic import BaseModel, Field, conlist
from layer8_auvik_api_client.models.device_relationships_device_detail import DeviceRelationshipsDeviceDetail
from layer8_auvik_api_client.models.device_relationships_networks import DeviceRelationshipsNetworks
from layer8_auvik_api_client.models.stack_all_of_relationships_all_of_members_inner import StackAllOfRelationshipsAllOfMembersInner
from layer8_auvik_api_client.models.tenant import Tenant

class StackAllOfRelationships(BaseModel):
    """
    StackAllOfRelationships
    """
    tenant: Optional[Tenant] = None
    networks: Optional[DeviceRelationshipsNetworks] = None
    device_detail: Optional[DeviceRelationshipsDeviceDetail] = Field(None, alias="deviceDetail")
    members: Optional[conlist(StackAllOfRelationshipsAllOfMembersInner)] = Field(None, description="Members of this stack")
    __properties = ["tenant", "networks", "deviceDetail", "members"]

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
    def from_json(cls, json_str: str) -> StackAllOfRelationships:
        """Create an instance of StackAllOfRelationships from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of tenant
        if self.tenant:
            _dict['tenant'] = self.tenant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of networks
        if self.networks:
            _dict['networks'] = self.networks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_detail
        if self.device_detail:
            _dict['deviceDetail'] = self.device_detail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item in self.members:
                if _item:
                    _items.append(_item.to_dict())
            _dict['members'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StackAllOfRelationships:
        """Create an instance of StackAllOfRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StackAllOfRelationships.parse_obj(obj)

        _obj = StackAllOfRelationships.parse_obj({
            "tenant": Tenant.from_dict(obj.get("tenant")) if obj.get("tenant") is not None else None,
            "networks": DeviceRelationshipsNetworks.from_dict(obj.get("networks")) if obj.get("networks") is not None else None,
            "device_detail": DeviceRelationshipsDeviceDetail.from_dict(obj.get("deviceDetail")) if obj.get("deviceDetail") is not None else None,
            "members": [StackAllOfRelationshipsAllOfMembersInner.from_dict(_item) for _item in obj.get("members")] if obj.get("members") is not None else None
        })
        return _obj



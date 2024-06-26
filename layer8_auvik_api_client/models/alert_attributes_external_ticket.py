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

class AlertAttributesExternalTicket(BaseModel):
    """
    AlertAttributesExternalTicket
    """
    id: Optional[StrictStr] = Field(None, description="The unique identifier for the external ticket")
    system: Optional[StrictStr] = Field(None, description="The system of external ticket")
    __properties = ["id", "system"]

    @validator('system')
    def system_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('All_User_Email', 'Single_User_Email', 'Custom_Email', 'Slack', 'Connectwise_Cloud', 'Connectwise_Premise', 'Freshdesk', 'Autotask', 'Map', 'Custom_Email_Group', 'Webhook', 'Microsoft_Teams', 'Continum', 'Connectwise_rest_Cloud', 'Servicenow'):
            raise ValueError("must be one of enum values ('All_User_Email', 'Single_User_Email', 'Custom_Email', 'Slack', 'Connectwise_Cloud', 'Connectwise_Premise', 'Freshdesk', 'Autotask', 'Map', 'Custom_Email_Group', 'Webhook', 'Microsoft_Teams', 'Continum', 'Connectwise_rest_Cloud', 'Servicenow')")
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
    def from_json(cls, json_str: str) -> AlertAttributesExternalTicket:
        """Create an instance of AlertAttributesExternalTicket from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlertAttributesExternalTicket:
        """Create an instance of AlertAttributesExternalTicket from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlertAttributesExternalTicket.parse_obj(obj)

        _obj = AlertAttributesExternalTicket.parse_obj({
            "id": obj.get("id"),
            "system": obj.get("system")
        })
        return _obj



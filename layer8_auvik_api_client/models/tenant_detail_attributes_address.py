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

class TenantDetailAttributesAddress(BaseModel):
    """
    Address of the tenant  # noqa: E501
    """
    address1: Optional[StrictStr] = Field(None, description="Tenant's mailing address")
    address2: Optional[StrictStr] = Field(None, description="Additional address information")
    city: Optional[StrictStr] = Field(None, description="City tenant is located in")
    state_province: Optional[StrictStr] = Field(None, alias="State/Province", description="State or region tenant is located in")
    zip_postal_code: Optional[StrictStr] = Field(None, alias="ZIP/PostalCode", description="Zip code or postal code of tenant's mailing address")
    state: Optional[StrictStr] = Field(None, description="State or region tenant is located in")
    postal_code: Optional[StrictStr] = Field(None, alias="postalCode", description="Zip code or postal code of tenant's mailing address")
    country: Optional[StrictStr] = Field(None, description="Country tenant is located in")
    __properties = ["address1", "address2", "city", "State/Province", "ZIP/PostalCode", "state", "postalCode", "country"]

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
    def from_json(cls, json_str: str) -> TenantDetailAttributesAddress:
        """Create an instance of TenantDetailAttributesAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TenantDetailAttributesAddress:
        """Create an instance of TenantDetailAttributesAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TenantDetailAttributesAddress.parse_obj(obj)

        _obj = TenantDetailAttributesAddress.parse_obj({
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "city": obj.get("city"),
            "state_province": obj.get("State/Province"),
            "zip_postal_code": obj.get("ZIP/PostalCode"),
            "state": obj.get("state"),
            "postal_code": obj.get("postalCode"),
            "country": obj.get("country")
        })
        return _obj


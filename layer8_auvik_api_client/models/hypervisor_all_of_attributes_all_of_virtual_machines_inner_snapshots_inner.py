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



from pydantic import BaseModel, Field, StrictStr

class HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner(BaseModel):
    """
    HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner
    """
    snapshot_name: StrictStr = Field(..., alias="snapshotName", description="The snapshot's name")
    snapshot_description: StrictStr = Field(..., alias="snapshotDescription", description="The snapshot's description")
    snapshot_date: StrictStr = Field(..., alias="snapshotDate", description="The date the snapshot was taken")
    snapshot_size: StrictStr = Field(..., alias="snapshotSize", description="File size of the snapshot")
    parent_snapshot_name: StrictStr = Field(..., alias="parentSnapshotName", description="Parent snapshot's name")
    __properties = ["snapshotName", "snapshotDescription", "snapshotDate", "snapshotSize", "parentSnapshotName"]

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
    def from_json(cls, json_str: str) -> HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner:
        """Create an instance of HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner:
        """Create an instance of HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner.parse_obj(obj)

        _obj = HypervisorAllOfAttributesAllOfVirtualMachinesInnerSnapshotsInner.parse_obj({
            "snapshot_name": obj.get("snapshotName"),
            "snapshot_description": obj.get("snapshotDescription"),
            "snapshot_date": obj.get("snapshotDate"),
            "snapshot_size": obj.get("snapshotSize"),
            "parent_snapshot_name": obj.get("parentSnapshotName")
        })
        return _obj



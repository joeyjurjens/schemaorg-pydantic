from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Number, Text
from .medical_intangible import MedicalIntangible


class MedicalConditionStage(MedicalIntangible):
    """A stage of a medical condition, such as 'Stage IIIa'."""
    schema_type: ClassVar[str] = "MedicalConditionStage"
    stage_as_number: Number | list[Number] | None = Field(default=None, validation_alias="stageAsNumber", serialization_alias="stageAsNumber")
    sub_stage_suffix: Text | list[Text] | None = Field(default=None, validation_alias="subStageSuffix", serialization_alias="subStageSuffix")

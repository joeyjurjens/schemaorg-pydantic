from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    MedicalEntity_Ref = Union[MedicalEntity, Ref]
else:
    MedicalEntity_Ref = Union[Is["MedicalEntity"], Ref]


class MedicalRiskFactor(MedicalEntity):
    """A risk factor is anything that increases a person's likelihood of developing or contracting a disease, medical condition, or complication."""
    schema_type: ClassVar[str] = "MedicalRiskFactor"
    increases_risk_of: MedicalEntity_Ref | list[MedicalEntity_Ref] | None = Field(default=None, validation_alias="increasesRiskOf", serialization_alias="increasesRiskOf")

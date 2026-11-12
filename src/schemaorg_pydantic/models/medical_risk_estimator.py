from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    from .medical_risk_factor import MedicalRiskFactor

if TYPE_CHECKING:
    MedicalEntity_Ref = Union[MedicalEntity, Ref]
else:
    MedicalEntity_Ref = Union[Is["MedicalEntity"], Ref]

if TYPE_CHECKING:
    MedicalRiskFactor_Ref = Union[MedicalRiskFactor, Ref]
else:
    MedicalRiskFactor_Ref = Union[Is["MedicalRiskFactor"], Ref]


class MedicalRiskEstimator(MedicalEntity):
    """Any rule set or interactive tool for estimating the risk of developing a complication or condition."""
    schema_type: ClassVar[str] = "MedicalRiskEstimator"
    estimates_risk_of: MedicalEntity_Ref | list[MedicalEntity_Ref] | None = Field(default=None, validation_alias="estimatesRiskOf", serialization_alias="estimatesRiskOf")
    included_risk_factor: MedicalRiskFactor_Ref | list[MedicalRiskFactor_Ref] | None = Field(default=None, validation_alias="includedRiskFactor", serialization_alias="includedRiskFactor")

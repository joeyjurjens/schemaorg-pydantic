from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .medical_risk_estimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    """A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score."""
    schema_type: ClassVar[str] = "MedicalRiskScore"
    algorithm: Text | list[Text] | None = Field(default=None)

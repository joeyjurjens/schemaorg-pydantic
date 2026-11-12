from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_sign import MedicalSign


class VitalSign(MedicalSign):
    """Vital signs are measures of various physiological functions in order to assess the most basic body functions."""
    schema_type: ClassVar[str] = "VitalSign"

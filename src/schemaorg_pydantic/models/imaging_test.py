from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_test import MedicalTest
from .medical_imaging_technique import MedicalImagingTechnique


class ImagingTest(MedicalTest):
    """Any medical imaging modality typically used for diagnostic purposes."""
    schema_type: ClassVar[str] = "ImagingTest"
    imaging_technique: MedicalImagingTechnique | list[MedicalImagingTechnique] | None = Field(default=None, validation_alias="imagingTechnique", serialization_alias="imagingTechnique")

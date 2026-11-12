from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .medical_test import MedicalTest


class BloodTest(MedicalTest):
    """A medical test performed on a sample of a patient's blood."""
    schema_type: ClassVar[str] = "BloodTest"

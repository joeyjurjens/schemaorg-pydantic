from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .medical_test import MedicalTest


class PathologyTest(MedicalTest):
    """A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist."""
    schema_type: ClassVar[str] = "PathologyTest"
    tissue_sample: Text | list[Text] | None = Field(default=None, validation_alias="tissueSample", serialization_alias="tissueSample")

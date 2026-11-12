from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .qualitative_value import QualitativeValue


class BedType(QualitativeValue):
    """A type of bed. This is used for indicating the bed or beds available in an accommodation."""
    schema_type: ClassVar[str] = "BedType"

from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Number
from .civic_structure import CivicStructure
from .entertainment_business import EntertainmentBusiness


class MovieTheater(CivicStructure, EntertainmentBusiness):
    """A movie theater."""
    schema_type: ClassVar[str] = "MovieTheater"
    screen_count: Number | list[Number] | None = Field(default=None, validation_alias="screenCount", serialization_alias="screenCount")

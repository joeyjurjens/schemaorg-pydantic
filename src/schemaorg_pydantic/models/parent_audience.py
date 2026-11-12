from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Number
from .people_audience import PeopleAudience


class ParentAudience(PeopleAudience):
    """A set of characteristics describing parents, who can be interested in viewing some content."""
    schema_type: ClassVar[str] = "ParentAudience"
    child_max_age: Number | list[Number] | None = Field(default=None, validation_alias="childMaxAge", serialization_alias="childMaxAge")
    child_min_age: Number | list[Number] | None = Field(default=None, validation_alias="childMinAge", serialization_alias="childMinAge")

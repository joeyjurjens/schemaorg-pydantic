from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .aggregate_rating import AggregateRating


class EmployerAggregateRating(AggregateRating):
    """An aggregate rating of an Organization related to its role as an employer."""
    schema_type: ClassVar[str] = "EmployerAggregateRating"

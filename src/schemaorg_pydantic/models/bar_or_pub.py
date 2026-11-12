from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .food_establishment import FoodEstablishment


class BarOrPub(FoodEstablishment):
    """A bar or pub."""
    schema_type: ClassVar[str] = "BarOrPub"

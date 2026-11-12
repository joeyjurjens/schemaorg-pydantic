from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .food_establishment import FoodEstablishment


class Winery(FoodEstablishment):
    """A winery."""
    schema_type: ClassVar[str] = "Winery"

from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .food_establishment import FoodEstablishment


class Brewery(FoodEstablishment):
    """Brewery."""
    schema_type: ClassVar[str] = "Brewery"

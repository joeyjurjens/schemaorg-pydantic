from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .food_establishment import FoodEstablishment


class CafeOrCoffeeShop(FoodEstablishment):
    """A cafe or coffee shop."""
    schema_type: ClassVar[str] = "CafeOrCoffeeShop"

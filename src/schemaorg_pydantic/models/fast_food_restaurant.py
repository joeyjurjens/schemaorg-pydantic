from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .food_establishment import FoodEstablishment


class FastFoodRestaurant(FoodEstablishment):
    """A fast-food restaurant."""
    schema_type: ClassVar[str] = "FastFoodRestaurant"

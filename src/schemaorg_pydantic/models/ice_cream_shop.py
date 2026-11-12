from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .food_establishment import FoodEstablishment


class IceCreamShop(FoodEstablishment):
    """An ice cream shop."""
    schema_type: ClassVar[str] = "IceCreamShop"

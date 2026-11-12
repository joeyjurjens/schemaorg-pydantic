from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .food_establishment import FoodEstablishment


class Bakery(FoodEstablishment):
    """A bakery."""
    schema_type: ClassVar[str] = "Bakery"

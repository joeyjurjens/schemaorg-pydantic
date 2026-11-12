from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .food_establishment import FoodEstablishment


class Distillery(FoodEstablishment):
    """A distillery."""
    schema_type: ClassVar[str] = "Distillery"

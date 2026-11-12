from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .service import Service


class FoodService(Service):
    """A food service, like breakfast, lunch, or dinner."""
    schema_type: ClassVar[str] = "FoodService"

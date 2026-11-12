from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class TireShop(Store):
    """A tire shop."""
    schema_type: ClassVar[str] = "TireShop"

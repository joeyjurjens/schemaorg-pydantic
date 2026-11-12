from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class SportingGoodsStore(Store):
    """A sporting goods store."""
    schema_type: ClassVar[str] = "SportingGoodsStore"

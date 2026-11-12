from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class HomeGoodsStore(Store):
    """A home goods store."""
    schema_type: ClassVar[str] = "HomeGoodsStore"

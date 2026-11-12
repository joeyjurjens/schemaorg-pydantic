from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class WholesaleStore(Store):
    """A wholesale store."""
    schema_type: ClassVar[str] = "WholesaleStore"

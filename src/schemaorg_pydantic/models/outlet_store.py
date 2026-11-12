from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class OutletStore(Store):
    """An outlet store."""
    schema_type: ClassVar[str] = "OutletStore"

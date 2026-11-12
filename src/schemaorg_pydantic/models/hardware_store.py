from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class HardwareStore(Store):
    """A hardware store."""
    schema_type: ClassVar[str] = "HardwareStore"

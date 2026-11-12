from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .automotive_business import AutomotiveBusiness
from .store import Store


class AutoPartsStore(AutomotiveBusiness, Store):
    """An auto parts store."""
    schema_type: ClassVar[str] = "AutoPartsStore"

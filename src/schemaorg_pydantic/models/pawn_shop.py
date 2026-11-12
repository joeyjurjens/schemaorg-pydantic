from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class PawnShop(Store):
    """A shop that will buy, or lend money against the security of, personal possessions."""
    schema_type: ClassVar[str] = "PawnShop"

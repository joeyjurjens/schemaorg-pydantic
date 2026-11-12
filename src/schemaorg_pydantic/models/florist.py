from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class Florist(Store):
    """A florist."""
    schema_type: ClassVar[str] = "Florist"

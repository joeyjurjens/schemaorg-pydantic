from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class ToyStore(Store):
    """A toy store."""
    schema_type: ClassVar[str] = "ToyStore"

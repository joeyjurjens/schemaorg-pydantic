from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class MovieRentalStore(Store):
    """A movie rental store."""
    schema_type: ClassVar[str] = "MovieRentalStore"

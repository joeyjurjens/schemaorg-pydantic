from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .store import Store


class BookStore(Store):
    """A bookstore."""
    schema_type: ClassVar[str] = "BookStore"

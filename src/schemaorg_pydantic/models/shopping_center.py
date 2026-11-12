from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class ShoppingCenter(LocalBusiness):
    """A shopping center or mall."""
    schema_type: ClassVar[str] = "ShoppingCenter"

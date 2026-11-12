from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class Store(LocalBusiness):
    """A retail good store."""
    schema_type: ClassVar[str] = "Store"

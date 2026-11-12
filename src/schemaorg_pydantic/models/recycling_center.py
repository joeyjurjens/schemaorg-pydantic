from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class RecyclingCenter(LocalBusiness):
    """A recycling center."""
    schema_type: ClassVar[str] = "RecyclingCenter"

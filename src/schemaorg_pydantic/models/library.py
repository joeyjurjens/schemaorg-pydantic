from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class Library(LocalBusiness):
    """A library."""
    schema_type: ClassVar[str] = "Library"

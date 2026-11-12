from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class LibrarySystem(Organization):
    """A [[LibrarySystem]] is a collaborative system amongst several libraries."""
    schema_type: ClassVar[str] = "LibrarySystem"

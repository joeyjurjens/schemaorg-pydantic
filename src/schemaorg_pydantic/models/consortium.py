from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class Consortium(Organization):
    """A Consortium is a membership [[Organization]] whose members are typically Organizations."""
    schema_type: ClassVar[str] = "Consortium"

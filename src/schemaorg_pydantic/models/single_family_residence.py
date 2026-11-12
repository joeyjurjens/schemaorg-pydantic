from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .house import House


class SingleFamilyResidence(House):
    """Residence type: Single-family home."""
    schema_type: ClassVar[str] = "SingleFamilyResidence"

from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class Zoo(CivicStructure):
    """A zoo."""
    schema_type: ClassVar[str] = "Zoo"

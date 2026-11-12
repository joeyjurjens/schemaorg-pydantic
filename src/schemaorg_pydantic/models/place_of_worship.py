from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class PlaceOfWorship(CivicStructure):
    """Place of worship, such as a church, synagogue, or mosque."""
    schema_type: ClassVar[str] = "PlaceOfWorship"

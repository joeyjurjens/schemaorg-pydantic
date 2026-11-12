from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .civic_structure import CivicStructure


class PublicToilet(CivicStructure):
    """A public toilet is a room or small building containing one or more toilets (and possibly also urinals) which is available for use by the general public, or by customers or employees of certain businesses."""
    schema_type: ClassVar[str] = "PublicToilet"

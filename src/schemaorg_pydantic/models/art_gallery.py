from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .entertainment_business import EntertainmentBusiness


class ArtGallery(EntertainmentBusiness):
    """An art gallery."""
    schema_type: ClassVar[str] = "ArtGallery"

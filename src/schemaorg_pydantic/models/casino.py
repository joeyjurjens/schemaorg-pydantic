from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .entertainment_business import EntertainmentBusiness


class Casino(EntertainmentBusiness):
    """A casino."""
    schema_type: ClassVar[str] = "Casino"

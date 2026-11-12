from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .entertainment_business import EntertainmentBusiness


class ComedyClub(EntertainmentBusiness):
    """A comedy club."""
    schema_type: ClassVar[str] = "ComedyClub"

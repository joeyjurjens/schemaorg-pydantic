from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .entertainment_business import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    """A nightclub or discotheque."""
    schema_type: ClassVar[str] = "NightClub"

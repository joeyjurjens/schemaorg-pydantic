from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .entertainment_business import EntertainmentBusiness


class AmusementPark(EntertainmentBusiness):
    """An amusement park."""
    schema_type: ClassVar[str] = "AmusementPark"

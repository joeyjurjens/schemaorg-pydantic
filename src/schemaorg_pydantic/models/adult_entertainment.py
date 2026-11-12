from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .entertainment_business import EntertainmentBusiness


class AdultEntertainment(EntertainmentBusiness):
    """An adult entertainment establishment."""
    schema_type: ClassVar[str] = "AdultEntertainment"

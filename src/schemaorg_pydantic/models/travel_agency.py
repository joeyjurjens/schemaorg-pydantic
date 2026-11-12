from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class TravelAgency(LocalBusiness):
    """A travel agency."""
    schema_type: ClassVar[str] = "TravelAgency"

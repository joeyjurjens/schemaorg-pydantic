from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class TouristInformationCenter(LocalBusiness):
    """A tourist information center."""
    schema_type: ClassVar[str] = "TouristInformationCenter"

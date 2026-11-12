from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class SportsActivityLocation(LocalBusiness):
    """A sports location, such as a playing field."""
    schema_type: ClassVar[str] = "SportsActivityLocation"

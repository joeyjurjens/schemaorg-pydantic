from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class RadioStation(LocalBusiness):
    """A radio station."""
    schema_type: ClassVar[str] = "RadioStation"

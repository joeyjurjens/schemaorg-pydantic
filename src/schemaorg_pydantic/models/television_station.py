from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class TelevisionStation(LocalBusiness):
    """A television station."""
    schema_type: ClassVar[str] = "TelevisionStation"

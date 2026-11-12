from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .automotive_business import AutomotiveBusiness


class GasStation(AutomotiveBusiness):
    """A gas station."""
    schema_type: ClassVar[str] = "GasStation"

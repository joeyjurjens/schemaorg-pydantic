from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .automotive_business import AutomotiveBusiness


class AutoBodyShop(AutomotiveBusiness):
    """Auto body shop."""
    schema_type: ClassVar[str] = "AutoBodyShop"

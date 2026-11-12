from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .automotive_business import AutomotiveBusiness


class AutoDealer(AutomotiveBusiness):
    """An car dealership."""
    schema_type: ClassVar[str] = "AutoDealer"

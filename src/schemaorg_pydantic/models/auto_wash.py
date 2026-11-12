from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .automotive_business import AutomotiveBusiness


class AutoWash(AutomotiveBusiness):
    """A car wash business."""
    schema_type: ClassVar[str] = "AutoWash"

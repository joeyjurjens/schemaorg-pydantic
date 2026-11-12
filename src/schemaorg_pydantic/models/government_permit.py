from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .permit import Permit


class GovernmentPermit(Permit):
    """A permit issued by a government agency."""
    schema_type: ClassVar[str] = "GovernmentPermit"

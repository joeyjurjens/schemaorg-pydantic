from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class SelfStorage(LocalBusiness):
    """A self-storage facility."""
    schema_type: ClassVar[str] = "SelfStorage"

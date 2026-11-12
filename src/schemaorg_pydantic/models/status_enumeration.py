from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class StatusEnumeration(Enumeration):
    """Lists or enumerations dealing with status types."""
    schema_type: ClassVar[str] = "StatusEnumeration"

from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class SizeGroupEnumeration(Enumeration):
    """Enumerates common size groups for various product categories."""
    schema_type: ClassVar[str] = "SizeGroupEnumeration"

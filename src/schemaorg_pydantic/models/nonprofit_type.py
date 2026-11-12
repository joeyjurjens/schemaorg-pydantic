from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class NonprofitType(Enumeration):
    """NonprofitType enumerates several kinds of official non-profit types of which a non-profit organization can be."""
    schema_type: ClassVar[str] = "NonprofitType"

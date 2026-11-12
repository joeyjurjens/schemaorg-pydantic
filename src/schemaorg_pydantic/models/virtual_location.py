from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .intangible import Intangible


class VirtualLocation(Intangible):
    """An online or virtual location for attending events. For example, one may attend an online seminar or educational event. While a virtual location may be used as the location of an event, virtual locations should not be confused with physical locations in the real world."""
    schema_type: ClassVar[str] = "VirtualLocation"

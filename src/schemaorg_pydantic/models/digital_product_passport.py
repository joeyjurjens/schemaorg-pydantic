from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .certification import Certification


class DigitalProductPassport(Certification):
    """A digital product passport (DPP), a record containing information about a product's lifecycle, sustainability, and compliance."""
    schema_type: ClassVar[str] = "DigitalProductPassport"

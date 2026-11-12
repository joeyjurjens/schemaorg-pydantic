from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .legal_service import LegalService


class Attorney(LegalService):
    """Professional service: Attorney."""
    schema_type: ClassVar[str] = "Attorney"

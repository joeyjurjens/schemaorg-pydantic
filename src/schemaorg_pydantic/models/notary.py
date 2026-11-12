from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .legal_service import LegalService


class Notary(LegalService):
    """A notary."""
    schema_type: ClassVar[str] = "Notary"

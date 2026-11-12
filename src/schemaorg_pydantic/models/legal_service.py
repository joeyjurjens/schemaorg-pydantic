from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class LegalService(LocalBusiness):
    """A LegalService is a business that provides legally-oriented services, advice and representation, e.g. law firms."""
    schema_type: ClassVar[str] = "LegalService"

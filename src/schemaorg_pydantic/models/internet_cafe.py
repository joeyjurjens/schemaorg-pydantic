from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .local_business import LocalBusiness


class InternetCafe(LocalBusiness):
    """An internet cafe."""
    schema_type: ClassVar[str] = "InternetCafe"

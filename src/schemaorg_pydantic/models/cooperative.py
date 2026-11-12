from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organization import Organization


class Cooperative(Organization):
    """An organization that is a joint project of multiple organizations or persons."""
    schema_type: ClassVar[str] = "Cooperative"

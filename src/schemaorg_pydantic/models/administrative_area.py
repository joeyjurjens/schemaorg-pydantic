from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .place import Place


class AdministrativeArea(Place):
    """A geographical region, typically under the jurisdiction of a particular government."""
    schema_type: ClassVar[str] = "AdministrativeArea"

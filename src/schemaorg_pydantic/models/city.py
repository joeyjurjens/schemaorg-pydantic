from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .administrative_area import AdministrativeArea


class City(AdministrativeArea):
    """A city or town."""
    schema_type: ClassVar[str] = "City"

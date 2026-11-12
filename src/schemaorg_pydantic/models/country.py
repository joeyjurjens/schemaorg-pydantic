from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .administrative_area import AdministrativeArea


class Country(AdministrativeArea):
    """A country."""
    schema_type: ClassVar[str] = "Country"

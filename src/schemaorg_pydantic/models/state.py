from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .administrative_area import AdministrativeArea


class State(AdministrativeArea):
    """A state or province of a country."""
    schema_type: ClassVar[str] = "State"

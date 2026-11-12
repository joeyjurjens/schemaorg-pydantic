from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .civic_structure import CivicStructure


class Airport(CivicStructure):
    """An airport."""
    schema_type: ClassVar[str] = "Airport"
    iata_code: Text | list[Text] | None = Field(default=None, validation_alias="iataCode", serialization_alias="iataCode")
    icao_code: Text | list[Text] | None = Field(default=None, validation_alias="icaoCode", serialization_alias="icaoCode")

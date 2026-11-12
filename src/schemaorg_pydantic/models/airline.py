from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .organization import Organization
from .boarding_policy_type import BoardingPolicyType


class Airline(Organization):
    """An organization that provides flights for passengers."""
    schema_type: ClassVar[str] = "Airline"
    boarding_policy: BoardingPolicyType | list[BoardingPolicyType] | None = Field(default=None, validation_alias="boardingPolicy", serialization_alias="boardingPolicy")
    iata_code: Text | list[Text] | None = Field(default=None, validation_alias="iataCode", serialization_alias="iataCode")

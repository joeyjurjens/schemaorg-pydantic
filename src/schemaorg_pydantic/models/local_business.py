from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .organization import Organization
from .place import Place


class LocalBusiness(Organization, Place):
    """A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc."""
    schema_type: ClassVar[str] = "LocalBusiness"
    currencies_accepted: Text | list[Text] | None = Field(default=None, validation_alias="currenciesAccepted", serialization_alias="currenciesAccepted")
    floor_level: Text | list[Text] | None = Field(default=None, validation_alias="floorLevel", serialization_alias="floorLevel")
    opening_hours: Text | list[Text] | None = Field(default=None, validation_alias="openingHours", serialization_alias="openingHours")
    payment_accepted: Text | list[Text] | None = Field(default=None, validation_alias="paymentAccepted", serialization_alias="paymentAccepted")
    price_range: Text | list[Text] | None = Field(default=None, validation_alias="priceRange", serialization_alias="priceRange")

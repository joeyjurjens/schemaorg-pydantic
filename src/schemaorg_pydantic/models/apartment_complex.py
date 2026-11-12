from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Number, Ref, Text
from .residence import Residence

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

Boolean_Text = Union[Boolean, Text]
if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]


class ApartmentComplex(Residence):
    """Residence type: Apartment complex."""
    schema_type: ClassVar[str] = "ApartmentComplex"
    number_of_accommodation_units: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="numberOfAccommodationUnits", serialization_alias="numberOfAccommodationUnits")
    number_of_available_accommodation_units: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="numberOfAvailableAccommodationUnits", serialization_alias="numberOfAvailableAccommodationUnits")
    number_of_bedrooms: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="numberOfBedrooms", serialization_alias="numberOfBedrooms")
    pets_allowed: Boolean_Text | list[Boolean_Text] | None = Field(default=None, validation_alias="petsAllowed", serialization_alias="petsAllowed")

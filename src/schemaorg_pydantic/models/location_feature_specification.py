from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref
from .property_value import PropertyValue

if TYPE_CHECKING:
    from .opening_hours_specification import OpeningHoursSpecification

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    OpeningHoursSpecification_Ref = Union[OpeningHoursSpecification, Ref]
else:
    OpeningHoursSpecification_Ref = Union[Is["OpeningHoursSpecification"], Ref]


class LocationFeatureSpecification(PropertyValue):
    """Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality."""
    schema_type: ClassVar[str] = "LocationFeatureSpecification"
    hours_available: OpeningHoursSpecification_Ref | list[OpeningHoursSpecification_Ref] | None = Field(default=None, validation_alias="hoursAvailable", serialization_alias="hoursAvailable")
    valid_from: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validFrom", serialization_alias="validFrom")
    valid_through: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validThrough", serialization_alias="validThrough")

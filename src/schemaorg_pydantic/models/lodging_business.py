from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, DateTime, Is, Number, Ref, Text, Time
from .local_business import LocalBusiness

if TYPE_CHECKING:
    from .audience import Audience
    from .language import Language
    from .quantitative_value import QuantitativeValue
    from .rating import Rating

if TYPE_CHECKING:
    Audience_Ref = Union[Audience, Ref]
else:
    Audience_Ref = Union[Is["Audience"], Ref]

Boolean_Text = Union[Boolean, Text]
DateTime_Time = Union[DateTime, Time]
if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]

if TYPE_CHECKING:
    Rating_Ref = Union[Rating, Ref]
else:
    Rating_Ref = Union[Is["Rating"], Ref]


class LodgingBusiness(LocalBusiness):
    """A lodging business, such as a motel, hotel, or inn."""
    schema_type: ClassVar[str] = "LodgingBusiness"
    audience: Audience_Ref | list[Audience_Ref] | None = Field(default=None)
    available_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="availableLanguage", serialization_alias="availableLanguage")
    checkin_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="checkinTime", serialization_alias="checkinTime")
    checkout_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="checkoutTime", serialization_alias="checkoutTime")
    number_of_rooms: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="numberOfRooms", serialization_alias="numberOfRooms")
    pets_allowed: Boolean_Text | list[Boolean_Text] | None = Field(default=None, validation_alias="petsAllowed", serialization_alias="petsAllowed")
    star_rating: Rating_Ref | list[Rating_Ref] | None = Field(default=None, validation_alias="starRating", serialization_alias="starRating")

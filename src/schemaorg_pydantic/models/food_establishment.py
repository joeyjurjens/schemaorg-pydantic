from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Ref, Text
from .local_business import LocalBusiness

if TYPE_CHECKING:
    from .menu import Menu
    from .rating import Rating

Boolean_Text = Union[Boolean, Text]
if TYPE_CHECKING:
    Menu_Text_Ref = Union[Menu, Text, Ref]
else:
    Menu_Text_Ref = Union[Is["Menu"], Text, Ref]

if TYPE_CHECKING:
    Rating_Ref = Union[Rating, Ref]
else:
    Rating_Ref = Union[Is["Rating"], Ref]


class FoodEstablishment(LocalBusiness):
    """A food-related business."""
    schema_type: ClassVar[str] = "FoodEstablishment"
    accepts_reservations: Boolean_Text | list[Boolean_Text] | None = Field(default=None, validation_alias="acceptsReservations", serialization_alias="acceptsReservations")
    has_menu: Menu_Text_Ref | list[Menu_Text_Ref] | None = Field(default=None, validation_alias="hasMenu", serialization_alias="hasMenu")
    serves_cuisine: Text | list[Text] | None = Field(default=None, validation_alias="servesCuisine", serialization_alias="servesCuisine")
    star_rating: Rating_Ref | list[Rating_Ref] | None = Field(default=None, validation_alias="starRating", serialization_alias="starRating")

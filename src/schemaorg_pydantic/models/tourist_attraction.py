from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .place import Place

if TYPE_CHECKING:
    from .audience import Audience
    from .language import Language

if TYPE_CHECKING:
    Audience_Text_Ref = Union[Audience, Text, Ref]
else:
    Audience_Text_Ref = Union[Is["Audience"], Text, Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]


class TouristAttraction(Place):
    """A tourist attraction.  In principle any Thing can be a [[TouristAttraction]], from a [[Mountain]] and [[LandmarksOrHistoricalBuildings]] to a [[LocalBusiness]].  This Type can be used on its own to describe a general [[TouristAttraction]], or be used as an [[additionalType]] to add tourist attraction properties to any other type.  (See examples below)"""
    schema_type: ClassVar[str] = "TouristAttraction"
    available_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="availableLanguage", serialization_alias="availableLanguage")
    tourist_type: Audience_Text_Ref | list[Audience_Text_Ref] | None = Field(default=None, validation_alias="touristType", serialization_alias="touristType")

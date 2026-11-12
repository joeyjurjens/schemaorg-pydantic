from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .place import Place

if TYPE_CHECKING:
    from .audience import Audience
    from .tourist_attraction import TouristAttraction

if TYPE_CHECKING:
    Audience_Text_Ref = Union[Audience, Text, Ref]
else:
    Audience_Text_Ref = Union[Is["Audience"], Text, Ref]

if TYPE_CHECKING:
    TouristAttraction_Ref = Union[TouristAttraction, Ref]
else:
    TouristAttraction_Ref = Union[Is["TouristAttraction"], Ref]


class TouristDestination(Place):
    """A tourist destination. In principle any [[Place]] can be a [[TouristDestination]] from a [[City]], Region or [[Country]] to an [[AmusementPark]] or [[Hotel]]. This Type can be used on its own to describe a general [[TouristDestination]], or be used as an [[additionalType]] to add tourist relevant properties to any other [[Place]].  A [[TouristDestination]] is defined as a [[Place]] that contains, or is colocated with, one or more [[TouristAttraction]]s, often linked by a similar theme or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines Destination (main destination of a tourism trip) as the place visited that is central to the decision to take the trip.\n  (See examples below.)"""
    schema_type: ClassVar[str] = "TouristDestination"
    includes_attraction: TouristAttraction_Ref | list[TouristAttraction_Ref] | None = Field(default=None, validation_alias="includesAttraction", serialization_alias="includesAttraction")
    tourist_type: Audience_Text_Ref | list[Audience_Text_Ref] | None = Field(default=None, validation_alias="touristType", serialization_alias="touristType")

from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .trip import Trip

if TYPE_CHECKING:
    from .audience import Audience

if TYPE_CHECKING:
    Audience_Text_Ref = Union[Audience, Text, Ref]
else:
    Audience_Text_Ref = Union[Is["Audience"], Text, Ref]


class TouristTrip(Trip):
    """A tourist trip. A created itinerary of visits to one or more places of interest ([[TouristAttraction]]/[[TouristDestination]]) often linked by a similar theme, geographic area, or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines tourism trip as the Trip taken by visitors.\n  (See examples below.)"""
    schema_type: ClassVar[str] = "TouristTrip"
    tourist_type: Audience_Text_Ref | list[Audience_Text_Ref] | None = Field(default=None, validation_alias="touristType", serialization_alias="touristType")

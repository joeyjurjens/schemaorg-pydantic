from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Is, Ref, Time
from .intangible import Intangible

if TYPE_CHECKING:
    from .demand import Demand
    from .item_list import ItemList
    from .offer import Offer
    from .organization import Organization
    from .person import Person
    from .place import Place

DateTime_Time = Union[DateTime, Time]
if TYPE_CHECKING:
    Demand_Offer_Ref = Union[Demand, Offer, Ref]
else:
    Demand_Offer_Ref = Union[Is["Demand"], Is["Offer"], Ref]

if TYPE_CHECKING:
    ItemList_Place_Ref = Union[ItemList, Place, Ref]
else:
    ItemList_Place_Ref = Union[Is["ItemList"], Is["Place"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]

if TYPE_CHECKING:
    Trip_Ref = Union["Trip", Ref]
else:
    Trip_Ref = Union[Is["Trip"], Ref]


class Trip(Intangible):
    """A trip or journey. An itinerary of visits to one or more places."""
    schema_type: ClassVar[str] = "Trip"
    arrival_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="arrivalTime", serialization_alias="arrivalTime")
    departure_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="departureTime", serialization_alias="departureTime")
    itinerary: ItemList_Place_Ref | list[ItemList_Place_Ref] | None = Field(default=None)
    offers: Demand_Offer_Ref | list[Demand_Offer_Ref] | None = Field(default=None)
    part_of_trip: Trip_Ref | list[Trip_Ref] | None = Field(default=None, validation_alias="partOfTrip", serialization_alias="partOfTrip")
    provider: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    sub_trip: Trip_Ref | list[Trip_Ref] | None = Field(default=None, validation_alias="subTrip", serialization_alias="subTrip")
    trip_origin: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="tripOrigin", serialization_alias="tripOrigin")

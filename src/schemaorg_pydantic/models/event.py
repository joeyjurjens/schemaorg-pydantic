from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, DateTime, Integer, Is, Ref, Text, Time
from .thing import Thing
from .event_attendance_mode_enumeration import EventAttendanceModeEnumeration
from .event_status_type import EventStatusType

if TYPE_CHECKING:
    from .aggregate_rating import AggregateRating
    from .audience import Audience
    from .creative_work import CreativeWork
    from .defined_term import DefinedTerm
    from .demand import Demand
    from .grant import Grant
    from .language import Language
    from .offer import Offer
    from .organization import Organization
    from .performing_group import PerformingGroup
    from .person import Person
    from .place import Place
    from .postal_address import PostalAddress
    from .quantitative_value import QuantitativeValue
    from .review import Review
    from .schedule import Schedule
    from .virtual_location import VirtualLocation

if TYPE_CHECKING:
    AggregateRating_Ref = Union[AggregateRating, Ref]
else:
    AggregateRating_Ref = Union[Is["AggregateRating"], Ref]

if TYPE_CHECKING:
    Audience_Ref = Union[Audience, Ref]
else:
    Audience_Ref = Union[Is["Audience"], Ref]

if TYPE_CHECKING:
    CreativeWork_Ref = Union[CreativeWork, Ref]
else:
    CreativeWork_Ref = Union[Is["CreativeWork"], Ref]

Date_DateTime = Union[Date, DateTime]
DateTime_Time = Union[DateTime, Time]
if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]

if TYPE_CHECKING:
    Demand_Offer_Ref = Union[Demand, Offer, Ref]
else:
    Demand_Offer_Ref = Union[Is["Demand"], Is["Offer"], Ref]

if TYPE_CHECKING:
    Event_Ref = Union["Event", Ref]
else:
    Event_Ref = Union[Is["Event"], Ref]

if TYPE_CHECKING:
    Grant_Ref = Union[Grant, Ref]
else:
    Grant_Ref = Union[Is["Grant"], Ref]

if TYPE_CHECKING:
    Language_Text_Ref = Union[Language, Text, Ref]
else:
    Language_Text_Ref = Union[Is["Language"], Text, Ref]

if TYPE_CHECKING:
    Offer_Ref = Union[Offer, Ref]
else:
    Offer_Ref = Union[Is["Offer"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    PerformingGroup_Person_Ref = Union[PerformingGroup, Person, Ref]
else:
    PerformingGroup_Person_Ref = Union[Is["PerformingGroup"], Is["Person"], Ref]

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

if TYPE_CHECKING:
    R2967d0a9 = Union[Place, PostalAddress, VirtualLocation, Text, Ref]
else:
    R2967d0a9 = Union[Is["Place"], Is["PostalAddress"], Is["VirtualLocation"], Text, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]

if TYPE_CHECKING:
    Review_Ref = Union[Review, Ref]
else:
    Review_Ref = Union[Is["Review"], Ref]

if TYPE_CHECKING:
    Schedule_Ref = Union[Schedule, Ref]
else:
    Schedule_Ref = Union[Is["Schedule"], Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class Event(Thing):
    """An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the [[offers]] property. Repeated events may be structured as separate Event objects."""
    schema_type: ClassVar[str] = "Event"
    about: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    actor: PerformingGroup_Person_Ref | list[PerformingGroup_Person_Ref] | None = Field(default=None)
    aggregate_rating: AggregateRating_Ref | list[AggregateRating_Ref] | None = Field(default=None, validation_alias="aggregateRating", serialization_alias="aggregateRating")
    attendee: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    audience: Audience_Ref | list[Audience_Ref] | None = Field(default=None)
    composer: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    contributor: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    director: Person_Ref | list[Person_Ref] | None = Field(default=None)
    door_time: DateTime_Time | list[DateTime_Time] | None = Field(default=None, validation_alias="doorTime", serialization_alias="doorTime")
    duration: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    end_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="endDate", serialization_alias="endDate")
    event_attendance_mode: EventAttendanceModeEnumeration | list[EventAttendanceModeEnumeration] | None = Field(default=None, validation_alias="eventAttendanceMode", serialization_alias="eventAttendanceMode")
    event_schedule: Schedule_Ref | list[Schedule_Ref] | None = Field(default=None, validation_alias="eventSchedule", serialization_alias="eventSchedule")
    event_status: EventStatusType | list[EventStatusType] | None = Field(default=None, validation_alias="eventStatus", serialization_alias="eventStatus")
    funder: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    funding: Grant_Ref | list[Grant_Ref] | None = Field(default=None)
    has_participation_offer: Offer_Ref | list[Offer_Ref] | None = Field(default=None, validation_alias="hasParticipationOffer", serialization_alias="hasParticipationOffer")
    has_sponsorship_offer: Offer_Ref | list[Offer_Ref] | None = Field(default=None, validation_alias="hasSponsorshipOffer", serialization_alias="hasSponsorshipOffer")
    in_language: Language_Text_Ref | list[Language_Text_Ref] | None = Field(default=None, validation_alias="inLanguage", serialization_alias="inLanguage")
    is_accessible_for_free: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isAccessibleForFree", serialization_alias="isAccessibleForFree")
    keywords: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    location: R2967d0a9 | list[R2967d0a9] | None = Field(default=None)
    maximum_attendee_capacity: Integer | list[Integer] | None = Field(default=None, validation_alias="maximumAttendeeCapacity", serialization_alias="maximumAttendeeCapacity")
    maximum_physical_attendee_capacity: Integer | list[Integer] | None = Field(default=None, validation_alias="maximumPhysicalAttendeeCapacity", serialization_alias="maximumPhysicalAttendeeCapacity")
    maximum_virtual_attendee_capacity: Integer | list[Integer] | None = Field(default=None, validation_alias="maximumVirtualAttendeeCapacity", serialization_alias="maximumVirtualAttendeeCapacity")
    offers: Demand_Offer_Ref | list[Demand_Offer_Ref] | None = Field(default=None)
    organizer: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    performer: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    previous_start_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="previousStartDate", serialization_alias="previousStartDate")
    recorded_in: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="recordedIn", serialization_alias="recordedIn")
    remaining_attendee_capacity: Integer | list[Integer] | None = Field(default=None, validation_alias="remainingAttendeeCapacity", serialization_alias="remainingAttendeeCapacity")
    review: Review_Ref | list[Review_Ref] | None = Field(default=None)
    sponsor: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    start_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="startDate", serialization_alias="startDate")
    sub_event: Event_Ref | list[Event_Ref] | None = Field(default=None, validation_alias="subEvent", serialization_alias="subEvent")
    super_event: Event_Ref | list[Event_Ref] | None = Field(default=None, validation_alias="superEvent", serialization_alias="superEvent")
    translator: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    typical_age_range: Text | list[Text] | None = Field(default=None, validation_alias="typicalAgeRange", serialization_alias="typicalAgeRange")
    work_featured: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="workFeatured", serialization_alias="workFeatured")
    work_performed: CreativeWork_Ref | list[CreativeWork_Ref] | None = Field(default=None, validation_alias="workPerformed", serialization_alias="workPerformed")

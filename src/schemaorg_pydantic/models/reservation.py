from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import DateTime, Is, Number, Ref, Text
from .intangible import Intangible
from .reservation_status_type import ReservationStatusType

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person
    from .price_specification import PriceSpecification
    from .program_membership import ProgramMembership
    from .thing import Thing
    from .ticket import Ticket

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    PriceSpecification_Number_Text_Ref = Union[PriceSpecification, Number, Text, Ref]
else:
    PriceSpecification_Number_Text_Ref = Union[Is["PriceSpecification"], Number, Text, Ref]

if TYPE_CHECKING:
    ProgramMembership_Ref = Union[ProgramMembership, Ref]
else:
    ProgramMembership_Ref = Union[Is["ProgramMembership"], Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]

if TYPE_CHECKING:
    Ticket_Ref = Union[Ticket, Ref]
else:
    Ticket_Ref = Union[Is["Ticket"], Ref]


class Reservation(Intangible):
    """Describes a reservation for travel, dining or an event. Some reservations require tickets."""
    schema_type: ClassVar[str] = "Reservation"
    booking_time: DateTime | list[DateTime] | None = Field(default=None, validation_alias="bookingTime", serialization_alias="bookingTime")
    broker: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    modified_time: DateTime | list[DateTime] | None = Field(default=None, validation_alias="modifiedTime", serialization_alias="modifiedTime")
    price_currency: Text | list[Text] | None = Field(default=None, validation_alias="priceCurrency", serialization_alias="priceCurrency")
    program_membership_used: ProgramMembership_Ref | list[ProgramMembership_Ref] | None = Field(default=None, validation_alias="programMembershipUsed", serialization_alias="programMembershipUsed")
    provider: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    reservation_for: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="reservationFor", serialization_alias="reservationFor")
    reservation_id: Text | list[Text] | None = Field(default=None, validation_alias="reservationId", serialization_alias="reservationId")
    reservation_status: ReservationStatusType | list[ReservationStatusType] | None = Field(default=None, validation_alias="reservationStatus", serialization_alias="reservationStatus")
    reserved_ticket: Ticket_Ref | list[Ticket_Ref] | None = Field(default=None, validation_alias="reservedTicket", serialization_alias="reservedTicket")
    total_price: PriceSpecification_Number_Text_Ref | list[PriceSpecification_Number_Text_Ref] | None = Field(default=None, validation_alias="totalPrice", serialization_alias="totalPrice")
    under_name: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="underName", serialization_alias="underName")

from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Number, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person
    from .price_specification import PriceSpecification
    from .seat import Seat

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]

if TYPE_CHECKING:
    PriceSpecification_Number_Text_Ref = Union[PriceSpecification, Number, Text, Ref]
else:
    PriceSpecification_Number_Text_Ref = Union[Is["PriceSpecification"], Number, Text, Ref]

if TYPE_CHECKING:
    Seat_Ref = Union[Seat, Ref]
else:
    Seat_Ref = Union[Is["Seat"], Ref]


class Ticket(Intangible):
    """Used to describe a ticket to an event, a flight, a bus ride, etc."""
    schema_type: ClassVar[str] = "Ticket"
    date_issued: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="dateIssued", serialization_alias="dateIssued")
    issued_by: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="issuedBy", serialization_alias="issuedBy")
    price_currency: Text | list[Text] | None = Field(default=None, validation_alias="priceCurrency", serialization_alias="priceCurrency")
    ticket_number: Text | list[Text] | None = Field(default=None, validation_alias="ticketNumber", serialization_alias="ticketNumber")
    ticket_token: Text | list[Text] | None = Field(default=None, validation_alias="ticketToken", serialization_alias="ticketToken")
    ticketed_seat: Seat_Ref | list[Seat_Ref] | None = Field(default=None, validation_alias="ticketedSeat", serialization_alias="ticketedSeat")
    total_price: PriceSpecification_Number_Text_Ref | list[PriceSpecification_Number_Text_Ref] | None = Field(default=None, validation_alias="totalPrice", serialization_alias="totalPrice")
    under_name: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None, validation_alias="underName", serialization_alias="underName")

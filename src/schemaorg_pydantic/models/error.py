from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Text
from .instantaneous_event import InstantaneousEvent
from .action_status_type import ActionStatusType
from .event_status_type import EventStatusType
from .game_server_status import GameServerStatus
from .legal_force_status import LegalForceStatus
from .order_status import OrderStatus
from .payment_status_type import PaymentStatusType
from .reservation_status_type import ReservationStatusType

if TYPE_CHECKING:
    from .defined_term import DefinedTerm

if TYPE_CHECKING:
    R2d53b217 = Union[ActionStatusType, DefinedTerm, EventStatusType, GameServerStatus, LegalForceStatus, OrderStatus, PaymentStatusType, ReservationStatusType, Integer, Text, Ref]
else:
    R2d53b217 = Union[ActionStatusType, Is["DefinedTerm"], EventStatusType, GameServerStatus, LegalForceStatus, OrderStatus, PaymentStatusType, ReservationStatusType, Integer, Text, Ref]


class Error(InstantaneousEvent):
    """Representation of an Error."""
    schema_type: ClassVar[str] = "Error"
    error_code: R2d53b217 | list[R2d53b217] | None = Field(default=None, validation_alias="errorCode", serialization_alias="errorCode")

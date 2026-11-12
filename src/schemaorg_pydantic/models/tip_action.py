from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .trade_action import TradeAction

if TYPE_CHECKING:
    from .audience import Audience
    from .contact_point import ContactPoint
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    R5c65ac19 = Union[Audience, ContactPoint, Organization, Person, Ref]
else:
    R5c65ac19 = Union[Is["Audience"], Is["ContactPoint"], Is["Organization"], Is["Person"], Ref]


class TipAction(TradeAction):
    """The act of giving money voluntarily to a beneficiary in recognition of services rendered."""
    schema_type: ClassVar[str] = "TipAction"
    recipient: R5c65ac19 | list[R5c65ac19] | None = Field(default=None)

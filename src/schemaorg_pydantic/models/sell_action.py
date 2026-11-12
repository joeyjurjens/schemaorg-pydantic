from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .trade_action import TradeAction

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class SellAction(TradeAction):
    """The act of taking money from a buyer in exchange for goods or services rendered. An agent sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction."""
    schema_type: ClassVar[str] = "SellAction"
    buyer: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)

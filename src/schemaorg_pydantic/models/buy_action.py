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


class BuyAction(TradeAction):
    """The act of giving money to a seller in exchange for goods or services rendered. An agent buys an object, product, or service from a seller for a price. Reciprocal of SellAction."""
    schema_type: ClassVar[str] = "BuyAction"
    seller: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)

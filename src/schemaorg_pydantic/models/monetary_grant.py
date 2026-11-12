from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref
from .grant import Grant

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

if TYPE_CHECKING:
    MonetaryAmount_Number_Ref = Union[MonetaryAmount, Number, Ref]
else:
    MonetaryAmount_Number_Ref = Union[Is["MonetaryAmount"], Number, Ref]


class MonetaryGrant(Grant):
    """A monetary grant."""
    schema_type: ClassVar[str] = "MonetaryGrant"
    amount: MonetaryAmount_Number_Ref | list[MonetaryAmount_Number_Ref] | None = Field(default=None)

from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .transfer_action import TransferAction

if TYPE_CHECKING:
    from .person import Person

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]


class LendAction(TransferAction):
    """The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction."""
    schema_type: ClassVar[str] = "LendAction"
    borrower: Person_Ref | list[Person_Ref] | None = Field(default=None)

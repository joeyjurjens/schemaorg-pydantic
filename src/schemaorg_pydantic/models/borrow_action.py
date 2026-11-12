from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .transfer_action import TransferAction

if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class BorrowAction(TransferAction):
    """The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction."""
    schema_type: ClassVar[str] = "BorrowAction"
    lender: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)

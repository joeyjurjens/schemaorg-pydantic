from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .choose_action import ChooseAction

if TYPE_CHECKING:
    from .person import Person

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]


class VoteAction(ChooseAction):
    """The act of expressing a preference from a fixed/finite/structured set of choices/options."""
    schema_type: ClassVar[str] = "VoteAction"
    candidate: Person_Ref | list[Person_Ref] | None = Field(default=None)

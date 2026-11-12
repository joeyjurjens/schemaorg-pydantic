from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .achieve_action import AchieveAction

if TYPE_CHECKING:
    from .person import Person

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]


class LoseAction(AchieveAction):
    """The act of being defeated in a competitive activity."""
    schema_type: ClassVar[str] = "LoseAction"
    winner: Person_Ref | list[Person_Ref] | None = Field(default=None)

from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .action import Action

if TYPE_CHECKING:
    from .thing import Thing

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class UpdateAction(Action):
    """The act of managing by changing/editing the state of the object."""
    schema_type: ClassVar[str] = "UpdateAction"
    target_collection: Thing_Ref | list[Thing_Ref] | None = Field(default=None, validation_alias="targetCollection", serialization_alias="targetCollection")

from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .action import Action

if TYPE_CHECKING:
    from .place import Place

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]


class TransferAction(Action):
    """The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another."""
    schema_type: ClassVar[str] = "TransferAction"
    from_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="fromLocation", serialization_alias="fromLocation")
    to_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="toLocation", serialization_alias="toLocation")

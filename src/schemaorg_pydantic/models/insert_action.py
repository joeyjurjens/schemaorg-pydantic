from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .add_action import AddAction

if TYPE_CHECKING:
    from .place import Place

if TYPE_CHECKING:
    Place_Ref = Union[Place, Ref]
else:
    Place_Ref = Union[Is["Place"], Ref]


class InsertAction(AddAction):
    """The act of adding at a specific location in an ordered collection."""
    schema_type: ClassVar[str] = "InsertAction"
    to_location: Place_Ref | list[Place_Ref] | None = Field(default=None, validation_alias="toLocation", serialization_alias="toLocation")

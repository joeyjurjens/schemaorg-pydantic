from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .audio_object import AudioObject
from .book import Book

if TYPE_CHECKING:
    from .person import Person

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]


class Audiobook(AudioObject, Book):
    """An audiobook."""
    schema_type: ClassVar[str] = "Audiobook"
    read_by: Person_Ref | list[Person_Ref] | None = Field(default=None, validation_alias="readBy", serialization_alias="readBy")

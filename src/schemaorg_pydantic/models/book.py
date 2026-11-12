from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Integer, Is, Ref, Text
from .creative_work import CreativeWork
from .book_format_type import BookFormatType

if TYPE_CHECKING:
    from .person import Person

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]


class Book(CreativeWork):
    """A book."""
    schema_type: ClassVar[str] = "Book"
    abridged: Boolean | list[Boolean] | None = Field(default=None)
    book_edition: Text | list[Text] | None = Field(default=None, validation_alias="bookEdition", serialization_alias="bookEdition")
    book_format: BookFormatType | list[BookFormatType] | None = Field(default=None, validation_alias="bookFormat", serialization_alias="bookFormat")
    illustrator: Person_Ref | list[Person_Ref] | None = Field(default=None)
    isbn: Text | list[Text] | None = Field(default=None)
    number_of_pages: Integer | list[Integer] | None = Field(default=None, validation_alias="numberOfPages", serialization_alias="numberOfPages")

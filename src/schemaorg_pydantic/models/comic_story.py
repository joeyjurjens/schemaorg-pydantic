from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .person import Person

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]


class ComicStory(CreativeWork):
    """The term \"story\" is any indivisible, re-printable\n    \tunit of a comic, including the interior stories, covers, and backmatter. Most\n    \tcomics have at least two stories: a cover (ComicCoverArt) and an interior story."""
    schema_type: ClassVar[str] = "ComicStory"
    artist: Person_Ref | list[Person_Ref] | None = Field(default=None)
    colorist: Person_Ref | list[Person_Ref] | None = Field(default=None)
    inker: Person_Ref | list[Person_Ref] | None = Field(default=None)
    letterer: Person_Ref | list[Person_Ref] | None = Field(default=None)
    penciler: Person_Ref | list[Person_Ref] | None = Field(default=None)

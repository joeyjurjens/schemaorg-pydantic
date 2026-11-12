from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .publication_issue import PublicationIssue

if TYPE_CHECKING:
    from .person import Person

if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]


class ComicIssue(PublicationIssue):
    """Individual comic issues are serially published as\n    \tpart of a larger series. For the sake of consistency, even one-shot issues\n    \tbelong to a series comprised of a single issue. All comic issues can be\n    \tuniquely identified by: the combination of the name and volume number of the\n    \tseries to which the issue belongs; the issue number; and the variant\n    \tdescription of the issue (if any)."""
    schema_type: ClassVar[str] = "ComicIssue"
    artist: Person_Ref | list[Person_Ref] | None = Field(default=None)
    colorist: Person_Ref | list[Person_Ref] | None = Field(default=None)
    inker: Person_Ref | list[Person_Ref] | None = Field(default=None)
    letterer: Person_Ref | list[Person_Ref] | None = Field(default=None)
    penciler: Person_Ref | list[Person_Ref] | None = Field(default=None)
    variant_cover: Text | list[Text] | None = Field(default=None, validation_alias="variantCover", serialization_alias="variantCover")

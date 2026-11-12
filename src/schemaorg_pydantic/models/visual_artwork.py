from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Integer, Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .person import Person
    from .quantitative_value import QuantitativeValue

Integer_Text = Union[Integer, Text]
if TYPE_CHECKING:
    Person_Ref = Union[Person, Ref]
else:
    Person_Ref = Union[Is["Person"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class VisualArtwork(CreativeWork):
    """A work of art that is primarily visual in character."""
    schema_type: ClassVar[str] = "VisualArtwork"
    art_edition: Integer_Text | list[Integer_Text] | None = Field(default=None, validation_alias="artEdition", serialization_alias="artEdition")
    art_medium: Text | list[Text] | None = Field(default=None, validation_alias="artMedium", serialization_alias="artMedium")
    artform: Text | list[Text] | None = Field(default=None)
    artist: Person_Ref | list[Person_Ref] | None = Field(default=None)
    artwork_surface: Text | list[Text] | None = Field(default=None, validation_alias="artworkSurface", serialization_alias="artworkSurface")
    colorist: Person_Ref | list[Person_Ref] | None = Field(default=None)
    depth: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    height: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    inker: Person_Ref | list[Person_Ref] | None = Field(default=None)
    letterer: Person_Ref | list[Person_Ref] | None = Field(default=None)
    penciler: Person_Ref | list[Person_Ref] | None = Field(default=None)
    weight: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    width: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)

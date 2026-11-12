from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .intangible import Intangible

if TYPE_CHECKING:
    from .defined_term_set import DefinedTermSet
    from .thing import Thing

if TYPE_CHECKING:
    DefinedTermSet_Url_Ref = Union[DefinedTermSet, Url, Ref]
else:
    DefinedTermSet_Url_Ref = Union[Is["DefinedTermSet"], Url, Ref]

if TYPE_CHECKING:
    Thing_Ref = Union[Thing, Ref]
else:
    Thing_Ref = Union[Is["Thing"], Ref]


class DefinedTerm(Intangible):
    """A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term. Use the about property to specify what the term is about."""
    schema_type: ClassVar[str] = "DefinedTerm"
    about: Thing_Ref | list[Thing_Ref] | None = Field(default=None)
    in_defined_term_set: DefinedTermSet_Url_Ref | list[DefinedTermSet_Url_Ref] | None = Field(default=None, validation_alias="inDefinedTermSet", serialization_alias="inDefinedTermSet")
    term_code: Text | list[Text] | None = Field(default=None, validation_alias="termCode", serialization_alias="termCode")

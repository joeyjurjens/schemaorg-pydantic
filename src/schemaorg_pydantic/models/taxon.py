from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .thing import Thing

if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .property_value import PropertyValue

if TYPE_CHECKING:
    DefinedTerm_Ref = Union[DefinedTerm, Ref]
else:
    DefinedTerm_Ref = Union[Is["DefinedTerm"], Ref]

if TYPE_CHECKING:
    PropertyValue_Text_Ref = Union[PropertyValue, Text, Ref]
else:
    PropertyValue_Text_Ref = Union[Is["PropertyValue"], Text, Ref]

if TYPE_CHECKING:
    Taxon_Text_Ref = Union["Taxon", Text, Ref]
else:
    Taxon_Text_Ref = Union[Is["Taxon"], Text, Ref]


class Taxon(Thing):
    """A set of organisms asserted to represent a natural cohesive biological unit."""
    schema_type: ClassVar[str] = "Taxon"
    child_taxon: Taxon_Text_Ref | list[Taxon_Text_Ref] | None = Field(default=None, validation_alias="childTaxon", serialization_alias="childTaxon")
    has_defined_term: DefinedTerm_Ref | list[DefinedTerm_Ref] | None = Field(default=None, validation_alias="hasDefinedTerm", serialization_alias="hasDefinedTerm")
    parent_taxon: Taxon_Text_Ref | list[Taxon_Text_Ref] | None = Field(default=None, validation_alias="parentTaxon", serialization_alias="parentTaxon")
    taxon_rank: PropertyValue_Text_Ref | list[PropertyValue_Text_Ref] | None = Field(default=None, validation_alias="taxonRank", serialization_alias="taxonRank")

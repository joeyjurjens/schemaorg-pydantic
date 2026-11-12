from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .bio_chem_entity import BioChemEntity

if TYPE_CHECKING:
    from .anatomical_structure import AnatomicalStructure
    from .anatomical_system import AnatomicalSystem
    from .defined_term import DefinedTerm

if TYPE_CHECKING:
    R9a15e38d = Union[AnatomicalStructure, AnatomicalSystem, BioChemEntity, DefinedTerm, Ref]
else:
    R9a15e38d = Union[Is["AnatomicalStructure"], Is["AnatomicalSystem"], Is["BioChemEntity"], Is["DefinedTerm"], Ref]

if TYPE_CHECKING:
    BioChemEntity_Ref = Union[BioChemEntity, Ref]
else:
    BioChemEntity_Ref = Union[Is["BioChemEntity"], Ref]

if TYPE_CHECKING:
    Gene_Ref = Union["Gene", Ref]
else:
    Gene_Ref = Union[Is["Gene"], Ref]


class Gene(BioChemEntity):
    """A discrete unit of inheritance which affects one or more biological traits (Source: [https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene)). Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific RNA 21), A- (agouti genotype)."""
    schema_type: ClassVar[str] = "Gene"
    alternative_of: Gene_Ref | list[Gene_Ref] | None = Field(default=None, validation_alias="alternativeOf", serialization_alias="alternativeOf")
    encodes_bio_chem_entity: BioChemEntity_Ref | list[BioChemEntity_Ref] | None = Field(default=None, validation_alias="encodesBioChemEntity", serialization_alias="encodesBioChemEntity")
    expressed_in: R9a15e38d | list[R9a15e38d] | None = Field(default=None, validation_alias="expressedIn", serialization_alias="expressedIn")
    has_bio_polymer_sequence: Text | list[Text] | None = Field(default=None, validation_alias="hasBioPolymerSequence", serialization_alias="hasBioPolymerSequence")

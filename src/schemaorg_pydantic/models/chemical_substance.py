from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .bio_chem_entity import BioChemEntity

if TYPE_CHECKING:
    from .defined_term import DefinedTerm

if TYPE_CHECKING:
    DefinedTerm_Ref = Union[DefinedTerm, Ref]
else:
    DefinedTerm_Ref = Union[Is["DefinedTerm"], Ref]


class ChemicalSubstance(BioChemEntity):
    """A chemical substance is 'a portion of matter of constant composition, composed of molecular entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999))."""
    schema_type: ClassVar[str] = "ChemicalSubstance"
    chemical_composition: Text | list[Text] | None = Field(default=None, validation_alias="chemicalComposition", serialization_alias="chemicalComposition")
    chemical_role: DefinedTerm_Ref | list[DefinedTerm_Ref] | None = Field(default=None, validation_alias="chemicalRole", serialization_alias="chemicalRole")
    potential_use: DefinedTerm_Ref | list[DefinedTerm_Ref] | None = Field(default=None, validation_alias="potentialUse", serialization_alias="potentialUse")

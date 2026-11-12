from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .bio_chem_entity import BioChemEntity

if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    DefinedTerm_Ref = Union[DefinedTerm, Ref]
else:
    DefinedTerm_Ref = Union[Is["DefinedTerm"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class MolecularEntity(BioChemEntity):
    """Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity."""
    schema_type: ClassVar[str] = "MolecularEntity"
    chemical_role: DefinedTerm_Ref | list[DefinedTerm_Ref] | None = Field(default=None, validation_alias="chemicalRole", serialization_alias="chemicalRole")
    in_ch_i: Text | list[Text] | None = Field(default=None, validation_alias="inChI", serialization_alias="inChI")
    in_ch_i_key: Text | list[Text] | None = Field(default=None, validation_alias="inChIKey", serialization_alias="inChIKey")
    iupac_name: Text | list[Text] | None = Field(default=None, validation_alias="iupacName", serialization_alias="iupacName")
    molecular_formula: Text | list[Text] | None = Field(default=None, validation_alias="molecularFormula", serialization_alias="molecularFormula")
    molecular_weight: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="molecularWeight", serialization_alias="molecularWeight")
    monoisotopic_molecular_weight: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="monoisotopicMolecularWeight", serialization_alias="monoisotopicMolecularWeight")
    potential_use: DefinedTerm_Ref | list[DefinedTerm_Ref] | None = Field(default=None, validation_alias="potentialUse", serialization_alias="potentialUse")
    smiles: Text | list[Text] | None = Field(default=None)

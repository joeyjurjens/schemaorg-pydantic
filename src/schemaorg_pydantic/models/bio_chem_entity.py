from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .thing import Thing

if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .gene import Gene
    from .grant import Grant
    from .medical_condition import MedicalCondition
    from .property_value import PropertyValue
    from .taxon import Taxon

if TYPE_CHECKING:
    BioChemEntity_Ref = Union["BioChemEntity", Ref]
else:
    BioChemEntity_Ref = Union[Is["BioChemEntity"], Ref]

if TYPE_CHECKING:
    DefinedTerm_PropertyValue_Url_Ref = Union[DefinedTerm, PropertyValue, Url, Ref]
else:
    DefinedTerm_PropertyValue_Url_Ref = Union[Is["DefinedTerm"], Is["PropertyValue"], Url, Ref]

if TYPE_CHECKING:
    DefinedTerm_Ref = Union[DefinedTerm, Ref]
else:
    DefinedTerm_Ref = Union[Is["DefinedTerm"], Ref]

if TYPE_CHECKING:
    DefinedTerm_Taxon_Text_Ref = Union[DefinedTerm, Taxon, Text, Ref]
else:
    DefinedTerm_Taxon_Text_Ref = Union[Is["DefinedTerm"], Is["Taxon"], Text, Ref]

if TYPE_CHECKING:
    Gene_Ref = Union[Gene, Ref]
else:
    Gene_Ref = Union[Is["Gene"], Ref]

if TYPE_CHECKING:
    Grant_Ref = Union[Grant, Ref]
else:
    Grant_Ref = Union[Is["Grant"], Ref]

if TYPE_CHECKING:
    MedicalCondition_PropertyValue_Url_Ref = Union[MedicalCondition, PropertyValue, Url, Ref]
else:
    MedicalCondition_PropertyValue_Url_Ref = Union[Is["MedicalCondition"], Is["PropertyValue"], Url, Ref]

if TYPE_CHECKING:
    PropertyValue_Text_Ref = Union[PropertyValue, Text, Ref]
else:
    PropertyValue_Text_Ref = Union[Is["PropertyValue"], Text, Ref]


class BioChemEntity(Thing):
    """Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical; a synthetic chemical."""
    schema_type: ClassVar[str] = "BioChemEntity"
    associated_disease: MedicalCondition_PropertyValue_Url_Ref | list[MedicalCondition_PropertyValue_Url_Ref] | None = Field(default=None, validation_alias="associatedDisease", serialization_alias="associatedDisease")
    bio_chem_interaction: BioChemEntity_Ref | list[BioChemEntity_Ref] | None = Field(default=None, validation_alias="bioChemInteraction", serialization_alias="bioChemInteraction")
    bio_chem_similarity: BioChemEntity_Ref | list[BioChemEntity_Ref] | None = Field(default=None, validation_alias="bioChemSimilarity", serialization_alias="bioChemSimilarity")
    biological_role: DefinedTerm_Ref | list[DefinedTerm_Ref] | None = Field(default=None, validation_alias="biologicalRole", serialization_alias="biologicalRole")
    funding: Grant_Ref | list[Grant_Ref] | None = Field(default=None)
    has_bio_chem_entity_part: BioChemEntity_Ref | list[BioChemEntity_Ref] | None = Field(default=None, validation_alias="hasBioChemEntityPart", serialization_alias="hasBioChemEntityPart")
    has_molecular_function: DefinedTerm_PropertyValue_Url_Ref | list[DefinedTerm_PropertyValue_Url_Ref] | None = Field(default=None, validation_alias="hasMolecularFunction", serialization_alias="hasMolecularFunction")
    has_representation: PropertyValue_Text_Ref | list[PropertyValue_Text_Ref] | None = Field(default=None, validation_alias="hasRepresentation", serialization_alias="hasRepresentation")
    is_encoded_by_bio_chem_entity: Gene_Ref | list[Gene_Ref] | None = Field(default=None, validation_alias="isEncodedByBioChemEntity", serialization_alias="isEncodedByBioChemEntity")
    is_involved_in_biological_process: DefinedTerm_PropertyValue_Url_Ref | list[DefinedTerm_PropertyValue_Url_Ref] | None = Field(default=None, validation_alias="isInvolvedInBiologicalProcess", serialization_alias="isInvolvedInBiologicalProcess")
    is_located_in_subcellular_location: DefinedTerm_PropertyValue_Url_Ref | list[DefinedTerm_PropertyValue_Url_Ref] | None = Field(default=None, validation_alias="isLocatedInSubcellularLocation", serialization_alias="isLocatedInSubcellularLocation")
    is_part_of_bio_chem_entity: BioChemEntity_Ref | list[BioChemEntity_Ref] | None = Field(default=None, validation_alias="isPartOfBioChemEntity", serialization_alias="isPartOfBioChemEntity")
    taxonomic_range: DefinedTerm_Taxon_Text_Ref | list[DefinedTerm_Taxon_Text_Ref] | None = Field(default=None, validation_alias="taxonomicRange", serialization_alias="taxonomicRange")

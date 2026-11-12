from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    from .anatomical_structure import AnatomicalStructure
    from .medical_condition import MedicalCondition
    from .medical_therapy import MedicalTherapy

if TYPE_CHECKING:
    AnatomicalStructure_AnatomicalSystem_Ref = Union[AnatomicalStructure, "AnatomicalSystem", Ref]
else:
    AnatomicalStructure_AnatomicalSystem_Ref = Union[Is["AnatomicalStructure"], Is["AnatomicalSystem"], Ref]

if TYPE_CHECKING:
    AnatomicalStructure_Ref = Union[AnatomicalStructure, Ref]
else:
    AnatomicalStructure_Ref = Union[Is["AnatomicalStructure"], Ref]

if TYPE_CHECKING:
    MedicalCondition_Ref = Union[MedicalCondition, Ref]
else:
    MedicalCondition_Ref = Union[Is["MedicalCondition"], Ref]

if TYPE_CHECKING:
    MedicalTherapy_Ref = Union[MedicalTherapy, Ref]
else:
    MedicalTherapy_Ref = Union[Is["MedicalTherapy"], Ref]


class AnatomicalSystem(MedicalEntity):
    """An anatomical system is a group of anatomical structures that work together to perform a certain task. Anatomical systems, such as organ systems, are one organizing principle of anatomy, and can include circulatory, digestive, endocrine, integumentary, immune, lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary, vestibular, and other systems."""
    schema_type: ClassVar[str] = "AnatomicalSystem"
    associated_pathophysiology: Text | list[Text] | None = Field(default=None, validation_alias="associatedPathophysiology", serialization_alias="associatedPathophysiology")
    comprised_of: AnatomicalStructure_AnatomicalSystem_Ref | list[AnatomicalStructure_AnatomicalSystem_Ref] | None = Field(default=None, validation_alias="comprisedOf", serialization_alias="comprisedOf")
    related_condition: MedicalCondition_Ref | list[MedicalCondition_Ref] | None = Field(default=None, validation_alias="relatedCondition", serialization_alias="relatedCondition")
    related_structure: AnatomicalStructure_Ref | list[AnatomicalStructure_Ref] | None = Field(default=None, validation_alias="relatedStructure", serialization_alias="relatedStructure")
    related_therapy: MedicalTherapy_Ref | list[MedicalTherapy_Ref] | None = Field(default=None, validation_alias="relatedTherapy", serialization_alias="relatedTherapy")

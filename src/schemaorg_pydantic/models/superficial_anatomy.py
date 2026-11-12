from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    from .anatomical_structure import AnatomicalStructure
    from .anatomical_system import AnatomicalSystem
    from .medical_condition import MedicalCondition
    from .medical_therapy import MedicalTherapy

if TYPE_CHECKING:
    AnatomicalStructure_AnatomicalSystem_Ref = Union[AnatomicalStructure, AnatomicalSystem, Ref]
else:
    AnatomicalStructure_AnatomicalSystem_Ref = Union[Is["AnatomicalStructure"], Is["AnatomicalSystem"], Ref]

if TYPE_CHECKING:
    MedicalCondition_Ref = Union[MedicalCondition, Ref]
else:
    MedicalCondition_Ref = Union[Is["MedicalCondition"], Ref]

if TYPE_CHECKING:
    MedicalTherapy_Ref = Union[MedicalTherapy, Ref]
else:
    MedicalTherapy_Ref = Union[Is["MedicalTherapy"], Ref]


class SuperficialAnatomy(MedicalEntity):
    """Anatomical features that can be observed by sight (without dissection), including the form and proportions of the human body as well as surface landmarks that correspond to deeper subcutaneous structures. Superficial anatomy plays an important role in sports medicine, phlebotomy, and other medical specialties as underlying anatomical structures can be identified through surface palpation. For example, during back surgery, superficial anatomy can be used to palpate and count vertebrae to find the site of incision. Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example, the median cubital vein can be located by palpating the borders of the cubital fossa (such as the epicondyles of the humerus) and then looking for the superficial signs of the vein, such as size, prominence, ability to refill after depression, and feel of surrounding tissue support. As another example, in a subluxation (dislocation) of the glenohumeral joint, the bony structure becomes pronounced with the deltoid muscle failing to cover the glenohumeral joint allowing the edges of the scapula to be superficially visible. Here, the superficial anatomy is the visible edges of the scapula, implying the underlying dislocation of the joint (the related anatomical structure)."""
    schema_type: ClassVar[str] = "SuperficialAnatomy"
    associated_pathophysiology: Text | list[Text] | None = Field(default=None, validation_alias="associatedPathophysiology", serialization_alias="associatedPathophysiology")
    related_anatomy: AnatomicalStructure_AnatomicalSystem_Ref | list[AnatomicalStructure_AnatomicalSystem_Ref] | None = Field(default=None, validation_alias="relatedAnatomy", serialization_alias="relatedAnatomy")
    related_condition: MedicalCondition_Ref | list[MedicalCondition_Ref] | None = Field(default=None, validation_alias="relatedCondition", serialization_alias="relatedCondition")
    related_therapy: MedicalTherapy_Ref | list[MedicalTherapy_Ref] | None = Field(default=None, validation_alias="relatedTherapy", serialization_alias="relatedTherapy")
    significance: Text | list[Text] | None = Field(default=None)

from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    from .anatomical_system import AnatomicalSystem
    from .image_object import ImageObject
    from .medical_condition import MedicalCondition
    from .medical_therapy import MedicalTherapy

if TYPE_CHECKING:
    AnatomicalStructure_Ref = Union["AnatomicalStructure", Ref]
else:
    AnatomicalStructure_Ref = Union[Is["AnatomicalStructure"], Ref]

if TYPE_CHECKING:
    AnatomicalSystem_Ref = Union[AnatomicalSystem, Ref]
else:
    AnatomicalSystem_Ref = Union[Is["AnatomicalSystem"], Ref]

if TYPE_CHECKING:
    ImageObject_Ref = Union[ImageObject, Ref]
else:
    ImageObject_Ref = Union[Is["ImageObject"], Ref]

if TYPE_CHECKING:
    MedicalCondition_Ref = Union[MedicalCondition, Ref]
else:
    MedicalCondition_Ref = Union[Is["MedicalCondition"], Ref]

if TYPE_CHECKING:
    MedicalTherapy_Ref = Union[MedicalTherapy, Ref]
else:
    MedicalTherapy_Ref = Union[Is["MedicalTherapy"], Ref]


class AnatomicalStructure(MedicalEntity):
    """Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures."""
    schema_type: ClassVar[str] = "AnatomicalStructure"
    associated_pathophysiology: Text | list[Text] | None = Field(default=None, validation_alias="associatedPathophysiology", serialization_alias="associatedPathophysiology")
    body_location: Text | list[Text] | None = Field(default=None, validation_alias="bodyLocation", serialization_alias="bodyLocation")
    connected_to: AnatomicalStructure_Ref | list[AnatomicalStructure_Ref] | None = Field(default=None, validation_alias="connectedTo", serialization_alias="connectedTo")
    diagram: ImageObject_Ref | list[ImageObject_Ref] | None = Field(default=None)
    part_of_system: AnatomicalSystem_Ref | list[AnatomicalSystem_Ref] | None = Field(default=None, validation_alias="partOfSystem", serialization_alias="partOfSystem")
    related_condition: MedicalCondition_Ref | list[MedicalCondition_Ref] | None = Field(default=None, validation_alias="relatedCondition", serialization_alias="relatedCondition")
    related_therapy: MedicalTherapy_Ref | list[MedicalTherapy_Ref] | None = Field(default=None, validation_alias="relatedTherapy", serialization_alias="relatedTherapy")
    sub_structure: AnatomicalStructure_Ref | list[AnatomicalStructure_Ref] | None = Field(default=None, validation_alias="subStructure", serialization_alias="subStructure")

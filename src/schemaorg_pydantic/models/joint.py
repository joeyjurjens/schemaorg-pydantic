from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .anatomical_structure import AnatomicalStructure

if TYPE_CHECKING:
    from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    MedicalEntity_Text_Ref = Union[MedicalEntity, Text, Ref]
else:
    MedicalEntity_Text_Ref = Union[Is["MedicalEntity"], Text, Ref]


class Joint(AnatomicalStructure):
    """The anatomical location at which two or more bones make contact."""
    schema_type: ClassVar[str] = "Joint"
    biomechnical_class: Text | list[Text] | None = Field(default=None, validation_alias="biomechnicalClass", serialization_alias="biomechnicalClass")
    functional_class: MedicalEntity_Text_Ref | list[MedicalEntity_Text_Ref] | None = Field(default=None, validation_alias="functionalClass", serialization_alias="functionalClass")
    structural_class: Text | list[Text] | None = Field(default=None, validation_alias="structuralClass", serialization_alias="structuralClass")

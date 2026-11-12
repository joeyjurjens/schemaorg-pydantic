from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .lifestyle_modification import LifestyleModification
from .physical_activity_category import PhysicalActivityCategory

if TYPE_CHECKING:
    from .anatomical_structure import AnatomicalStructure
    from .anatomical_system import AnatomicalSystem
    from .category_code import CategoryCode
    from .superficial_anatomy import SuperficialAnatomy
    from .thing import Thing

if TYPE_CHECKING:
    AnatomicalStructure_AnatomicalSystem_SuperficialAnatomy_Ref = Union[AnatomicalStructure, AnatomicalSystem, SuperficialAnatomy, Ref]
else:
    AnatomicalStructure_AnatomicalSystem_SuperficialAnatomy_Ref = Union[Is["AnatomicalStructure"], Is["AnatomicalSystem"], Is["SuperficialAnatomy"], Ref]

if TYPE_CHECKING:
    R88d1e012 = Union[CategoryCode, PhysicalActivityCategory, Thing, Text, Ref]
else:
    R88d1e012 = Union[Is["CategoryCode"], PhysicalActivityCategory, Is["Thing"], Text, Ref]


class PhysicalActivity(LifestyleModification):
    """Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan."""
    schema_type: ClassVar[str] = "PhysicalActivity"
    associated_anatomy: AnatomicalStructure_AnatomicalSystem_SuperficialAnatomy_Ref | list[AnatomicalStructure_AnatomicalSystem_SuperficialAnatomy_Ref] | None = Field(default=None, validation_alias="associatedAnatomy", serialization_alias="associatedAnatomy")
    category: R88d1e012 | list[R88d1e012] | None = Field(default=None)
    epidemiology: Text | list[Text] | None = Field(default=None)
    pathophysiology: Text | list[Text] | None = Field(default=None)

from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .anatomical_structure import AnatomicalStructure

if TYPE_CHECKING:
    from .brain_structure import BrainStructure
    from .muscle import Muscle
    from .superficial_anatomy import SuperficialAnatomy

if TYPE_CHECKING:
    AnatomicalStructure_SuperficialAnatomy_Ref = Union[AnatomicalStructure, SuperficialAnatomy, Ref]
else:
    AnatomicalStructure_SuperficialAnatomy_Ref = Union[Is["AnatomicalStructure"], Is["SuperficialAnatomy"], Ref]

if TYPE_CHECKING:
    BrainStructure_Ref = Union[BrainStructure, Ref]
else:
    BrainStructure_Ref = Union[Is["BrainStructure"], Ref]

if TYPE_CHECKING:
    Muscle_Ref = Union[Muscle, Ref]
else:
    Muscle_Ref = Union[Is["Muscle"], Ref]


class Nerve(AnatomicalStructure):
    """A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons."""
    schema_type: ClassVar[str] = "Nerve"
    nerve_motor: Muscle_Ref | list[Muscle_Ref] | None = Field(default=None, validation_alias="nerveMotor", serialization_alias="nerveMotor")
    sensory_unit: AnatomicalStructure_SuperficialAnatomy_Ref | list[AnatomicalStructure_SuperficialAnatomy_Ref] | None = Field(default=None, validation_alias="sensoryUnit", serialization_alias="sensoryUnit")
    sourced_from: BrainStructure_Ref | list[BrainStructure_Ref] | None = Field(default=None, validation_alias="sourcedFrom", serialization_alias="sourcedFrom")

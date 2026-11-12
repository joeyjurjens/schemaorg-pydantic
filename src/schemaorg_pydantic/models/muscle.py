from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .anatomical_structure import AnatomicalStructure

if TYPE_CHECKING:
    from .nerve import Nerve
    from .vessel import Vessel

if TYPE_CHECKING:
    AnatomicalStructure_Ref = Union[AnatomicalStructure, Ref]
else:
    AnatomicalStructure_Ref = Union[Is["AnatomicalStructure"], Ref]

if TYPE_CHECKING:
    Muscle_Ref = Union["Muscle", Ref]
else:
    Muscle_Ref = Union[Is["Muscle"], Ref]

if TYPE_CHECKING:
    Nerve_Ref = Union[Nerve, Ref]
else:
    Nerve_Ref = Union[Is["Nerve"], Ref]

if TYPE_CHECKING:
    Vessel_Ref = Union[Vessel, Ref]
else:
    Vessel_Ref = Union[Is["Vessel"], Ref]


class Muscle(AnatomicalStructure):
    """A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement."""
    schema_type: ClassVar[str] = "Muscle"
    antagonist: Muscle_Ref | list[Muscle_Ref] | None = Field(default=None)
    blood_supply: Vessel_Ref | list[Vessel_Ref] | None = Field(default=None, validation_alias="bloodSupply", serialization_alias="bloodSupply")
    insertion: AnatomicalStructure_Ref | list[AnatomicalStructure_Ref] | None = Field(default=None)
    muscle_action: Text | list[Text] | None = Field(default=None, validation_alias="muscleAction", serialization_alias="muscleAction")
    nerve: Nerve_Ref | list[Nerve_Ref] | None = Field(default=None)

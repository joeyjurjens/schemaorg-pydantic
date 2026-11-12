from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .vessel import Vessel

if TYPE_CHECKING:
    from .anatomical_structure import AnatomicalStructure
    from .anatomical_system import AnatomicalSystem

if TYPE_CHECKING:
    AnatomicalStructure_AnatomicalSystem_Ref = Union[AnatomicalStructure, AnatomicalSystem, Ref]
else:
    AnatomicalStructure_AnatomicalSystem_Ref = Union[Is["AnatomicalStructure"], Is["AnatomicalSystem"], Ref]

if TYPE_CHECKING:
    AnatomicalStructure_Ref = Union[AnatomicalStructure, Ref]
else:
    AnatomicalStructure_Ref = Union[Is["AnatomicalStructure"], Ref]

if TYPE_CHECKING:
    Vessel_Ref = Union[Vessel, Ref]
else:
    Vessel_Ref = Union[Is["Vessel"], Ref]


class Vein(Vessel):
    """A type of blood vessel that specifically carries blood to the heart."""
    schema_type: ClassVar[str] = "Vein"
    drains_to: Vessel_Ref | list[Vessel_Ref] | None = Field(default=None, validation_alias="drainsTo", serialization_alias="drainsTo")
    region_drained: AnatomicalStructure_AnatomicalSystem_Ref | list[AnatomicalStructure_AnatomicalSystem_Ref] | None = Field(default=None, validation_alias="regionDrained", serialization_alias="regionDrained")
    tributary: AnatomicalStructure_Ref | list[AnatomicalStructure_Ref] | None = Field(default=None)

from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .vessel import Vessel

if TYPE_CHECKING:
    from .anatomical_structure import AnatomicalStructure

if TYPE_CHECKING:
    AnatomicalStructure_Ref = Union[AnatomicalStructure, Ref]
else:
    AnatomicalStructure_Ref = Union[Is["AnatomicalStructure"], Ref]


class Artery(Vessel):
    """A type of blood vessel that specifically carries blood away from the heart."""
    schema_type: ClassVar[str] = "Artery"
    arterial_branch: AnatomicalStructure_Ref | list[AnatomicalStructure_Ref] | None = Field(default=None, validation_alias="arterialBranch", serialization_alias="arterialBranch")
    supply_to: AnatomicalStructure_Ref | list[AnatomicalStructure_Ref] | None = Field(default=None, validation_alias="supplyTo", serialization_alias="supplyTo")

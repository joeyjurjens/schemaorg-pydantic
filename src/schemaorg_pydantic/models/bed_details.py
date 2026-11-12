from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .bed_type import BedType

if TYPE_CHECKING:
    BedType_Text_Ref = Union[BedType, Text, Ref]
else:
    BedType_Text_Ref = Union[Is["BedType"], Text, Ref]


class BedDetails(Intangible):
    """An entity holding detailed information about the available bed types, e.g. the quantity of twin beds for a hotel room. For the single case of just one bed of a certain type, you can use bed directly with a text. See also [[BedType]] (under development)."""
    schema_type: ClassVar[str] = "BedDetails"
    number_of_beds: Number | list[Number] | None = Field(default=None, validation_alias="numberOfBeds", serialization_alias="numberOfBeds")
    type_of_bed: BedType_Text_Ref | list[BedType_Text_Ref] | None = Field(default=None, validation_alias="typeOfBed", serialization_alias="typeOfBed")

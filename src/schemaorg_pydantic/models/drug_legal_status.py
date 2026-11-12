from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .medical_intangible import MedicalIntangible

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea

if TYPE_CHECKING:
    AdministrativeArea_Ref = Union[AdministrativeArea, Ref]
else:
    AdministrativeArea_Ref = Union[Is["AdministrativeArea"], Ref]


class DrugLegalStatus(MedicalIntangible):
    """The legal availability status of a medical drug."""
    schema_type: ClassVar[str] = "DrugLegalStatus"
    applicable_location: AdministrativeArea_Ref | list[AdministrativeArea_Ref] | None = Field(default=None, validation_alias="applicableLocation", serialization_alias="applicableLocation")

from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .medical_intangible import MedicalIntangible

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .maximum_dose_schedule import MaximumDoseSchedule

if TYPE_CHECKING:
    AdministrativeArea_Ref = Union[AdministrativeArea, Ref]
else:
    AdministrativeArea_Ref = Union[Is["AdministrativeArea"], Ref]

if TYPE_CHECKING:
    MaximumDoseSchedule_Ref = Union[MaximumDoseSchedule, Ref]
else:
    MaximumDoseSchedule_Ref = Union[Is["MaximumDoseSchedule"], Ref]


class DrugStrength(MedicalIntangible):
    """A specific strength in which a medical drug is available in a specific country."""
    schema_type: ClassVar[str] = "DrugStrength"
    active_ingredient: Text | list[Text] | None = Field(default=None, validation_alias="activeIngredient", serialization_alias="activeIngredient")
    available_in: AdministrativeArea_Ref | list[AdministrativeArea_Ref] | None = Field(default=None, validation_alias="availableIn", serialization_alias="availableIn")
    maximum_intake: MaximumDoseSchedule_Ref | list[MaximumDoseSchedule_Ref] | None = Field(default=None, validation_alias="maximumIntake", serialization_alias="maximumIntake")
    strength_unit: Text | list[Text] | None = Field(default=None, validation_alias="strengthUnit", serialization_alias="strengthUnit")
    strength_value: Number | list[Number] | None = Field(default=None, validation_alias="strengthValue", serialization_alias="strengthValue")

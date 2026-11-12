from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .medical_entity import MedicalEntity

if TYPE_CHECKING:
    from .maximum_dose_schedule import MaximumDoseSchedule

if TYPE_CHECKING:
    MaximumDoseSchedule_Ref = Union[MaximumDoseSchedule, Ref]
else:
    MaximumDoseSchedule_Ref = Union[Is["MaximumDoseSchedule"], Ref]


class Substance(MedicalEntity):
    """Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or chemical."""
    schema_type: ClassVar[str] = "Substance"
    active_ingredient: Text | list[Text] | None = Field(default=None, validation_alias="activeIngredient", serialization_alias="activeIngredient")
    maximum_intake: MaximumDoseSchedule_Ref | list[MaximumDoseSchedule_Ref] | None = Field(default=None, validation_alias="maximumIntake", serialization_alias="maximumIntake")

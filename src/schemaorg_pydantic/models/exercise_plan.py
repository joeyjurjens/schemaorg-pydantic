from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .creative_work import CreativeWork
from .physical_activity import PhysicalActivity

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class ExercisePlan(CreativeWork, PhysicalActivity):
    """Fitness-related activity designed for a specific health-related purpose, including defined exercise routines as well as activity prescribed by a clinician."""
    schema_type: ClassVar[str] = "ExercisePlan"
    activity_duration: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="activityDuration", serialization_alias="activityDuration")
    activity_frequency: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="activityFrequency", serialization_alias="activityFrequency")
    additional_variable: Text | list[Text] | None = Field(default=None, validation_alias="additionalVariable", serialization_alias="additionalVariable")
    exercise_type: Text | list[Text] | None = Field(default=None, validation_alias="exerciseType", serialization_alias="exerciseType")
    intensity: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    repetitions: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None)
    rest_periods: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="restPeriods", serialization_alias="restPeriods")
    workload: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)

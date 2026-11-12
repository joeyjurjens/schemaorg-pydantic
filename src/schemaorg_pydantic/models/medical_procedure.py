from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .medical_entity import MedicalEntity
from .event_status_type import EventStatusType
from .medical_procedure_type import MedicalProcedureType
from .medical_study_status import MedicalStudyStatus

EventStatusType_MedicalStudyStatus_Text = Union[EventStatusType, MedicalStudyStatus, Text]
if TYPE_CHECKING:
    MedicalEntity_Text_Ref = Union[MedicalEntity, Text, Ref]
else:
    MedicalEntity_Text_Ref = Union[Is["MedicalEntity"], Text, Ref]


class MedicalProcedure(MedicalEntity):
    """A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques."""
    schema_type: ClassVar[str] = "MedicalProcedure"
    body_location: Text | list[Text] | None = Field(default=None, validation_alias="bodyLocation", serialization_alias="bodyLocation")
    followup: Text | list[Text] | None = Field(default=None)
    how_performed: Text | list[Text] | None = Field(default=None, validation_alias="howPerformed", serialization_alias="howPerformed")
    preparation: MedicalEntity_Text_Ref | list[MedicalEntity_Text_Ref] | None = Field(default=None)
    procedure_type: MedicalProcedureType | list[MedicalProcedureType] | None = Field(default=None, validation_alias="procedureType", serialization_alias="procedureType")
    status: EventStatusType_MedicalStudyStatus_Text | list[EventStatusType_MedicalStudyStatus_Text] | None = Field(default=None)

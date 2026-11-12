from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .medical_entity import MedicalEntity
from .event_status_type import EventStatusType
from .medical_study_status import MedicalStudyStatus

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .medical_condition import MedicalCondition
    from .organization import Organization
    from .person import Person

if TYPE_CHECKING:
    AdministrativeArea_Ref = Union[AdministrativeArea, Ref]
else:
    AdministrativeArea_Ref = Union[Is["AdministrativeArea"], Ref]

EventStatusType_MedicalStudyStatus_Text = Union[EventStatusType, MedicalStudyStatus, Text]
if TYPE_CHECKING:
    MedicalCondition_Ref = Union[MedicalCondition, Ref]
else:
    MedicalCondition_Ref = Union[Is["MedicalCondition"], Ref]

if TYPE_CHECKING:
    MedicalEntity_Ref = Union[MedicalEntity, Ref]
else:
    MedicalEntity_Ref = Union[Is["MedicalEntity"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]


class MedicalStudy(MedicalEntity):
    """A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID."""
    schema_type: ClassVar[str] = "MedicalStudy"
    health_condition: MedicalCondition_Ref | list[MedicalCondition_Ref] | None = Field(default=None, validation_alias="healthCondition", serialization_alias="healthCondition")
    sponsor: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    status: EventStatusType_MedicalStudyStatus_Text | list[EventStatusType_MedicalStudyStatus_Text] | None = Field(default=None)
    study_location: AdministrativeArea_Ref | list[AdministrativeArea_Ref] | None = Field(default=None, validation_alias="studyLocation", serialization_alias="studyLocation")
    study_subject: MedicalEntity_Ref | list[MedicalEntity_Ref] | None = Field(default=None, validation_alias="studySubject", serialization_alias="studySubject")

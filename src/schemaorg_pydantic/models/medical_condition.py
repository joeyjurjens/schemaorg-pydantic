from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .medical_entity import MedicalEntity
from .event_status_type import EventStatusType
from .medical_study_status import MedicalStudyStatus

if TYPE_CHECKING:
    from .anatomical_structure import AnatomicalStructure
    from .anatomical_system import AnatomicalSystem
    from .d_dx_element import DDxElement
    from .drug import Drug
    from .drug_class import DrugClass
    from .lifestyle_modification import LifestyleModification
    from .medical_cause import MedicalCause
    from .medical_condition_stage import MedicalConditionStage
    from .medical_risk_factor import MedicalRiskFactor
    from .medical_sign_or_symptom import MedicalSignOrSymptom
    from .medical_test import MedicalTest
    from .medical_therapy import MedicalTherapy
    from .superficial_anatomy import SuperficialAnatomy

if TYPE_CHECKING:
    AnatomicalStructure_AnatomicalSystem_SuperficialAnatomy_Ref = Union[AnatomicalStructure, AnatomicalSystem, SuperficialAnatomy, Ref]
else:
    AnatomicalStructure_AnatomicalSystem_SuperficialAnatomy_Ref = Union[Is["AnatomicalStructure"], Is["AnatomicalSystem"], Is["SuperficialAnatomy"], Ref]

if TYPE_CHECKING:
    DDxElement_Ref = Union[DDxElement, Ref]
else:
    DDxElement_Ref = Union[Is["DDxElement"], Ref]

if TYPE_CHECKING:
    Rec646fde = Union[Drug, DrugClass, LifestyleModification, MedicalTherapy, Ref]
else:
    Rec646fde = Union[Is["Drug"], Is["DrugClass"], Is["LifestyleModification"], Is["MedicalTherapy"], Ref]

if TYPE_CHECKING:
    Drug_Ref = Union[Drug, Ref]
else:
    Drug_Ref = Union[Is["Drug"], Ref]

EventStatusType_MedicalStudyStatus_Text = Union[EventStatusType, MedicalStudyStatus, Text]
if TYPE_CHECKING:
    MedicalCause_Ref = Union[MedicalCause, Ref]
else:
    MedicalCause_Ref = Union[Is["MedicalCause"], Ref]

if TYPE_CHECKING:
    MedicalConditionStage_Ref = Union[MedicalConditionStage, Ref]
else:
    MedicalConditionStage_Ref = Union[Is["MedicalConditionStage"], Ref]

if TYPE_CHECKING:
    MedicalRiskFactor_Ref = Union[MedicalRiskFactor, Ref]
else:
    MedicalRiskFactor_Ref = Union[Is["MedicalRiskFactor"], Ref]

if TYPE_CHECKING:
    MedicalSignOrSymptom_Ref = Union[MedicalSignOrSymptom, Ref]
else:
    MedicalSignOrSymptom_Ref = Union[Is["MedicalSignOrSymptom"], Ref]

if TYPE_CHECKING:
    MedicalTest_Ref = Union[MedicalTest, Ref]
else:
    MedicalTest_Ref = Union[Is["MedicalTest"], Ref]

if TYPE_CHECKING:
    MedicalTherapy_Ref = Union[MedicalTherapy, Ref]
else:
    MedicalTherapy_Ref = Union[Is["MedicalTherapy"], Ref]


class MedicalCondition(MedicalEntity):
    """Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc."""
    schema_type: ClassVar[str] = "MedicalCondition"
    associated_anatomy: AnatomicalStructure_AnatomicalSystem_SuperficialAnatomy_Ref | list[AnatomicalStructure_AnatomicalSystem_SuperficialAnatomy_Ref] | None = Field(default=None, validation_alias="associatedAnatomy", serialization_alias="associatedAnatomy")
    cause: MedicalCause_Ref | list[MedicalCause_Ref] | None = Field(default=None)
    differential_diagnosis: DDxElement_Ref | list[DDxElement_Ref] | None = Field(default=None, validation_alias="differentialDiagnosis", serialization_alias="differentialDiagnosis")
    drug: Drug_Ref | list[Drug_Ref] | None = Field(default=None)
    epidemiology: Text | list[Text] | None = Field(default=None)
    expected_prognosis: Text | list[Text] | None = Field(default=None, validation_alias="expectedPrognosis", serialization_alias="expectedPrognosis")
    natural_progression: Text | list[Text] | None = Field(default=None, validation_alias="naturalProgression", serialization_alias="naturalProgression")
    pathophysiology: Text | list[Text] | None = Field(default=None)
    possible_complication: Text | list[Text] | None = Field(default=None, validation_alias="possibleComplication", serialization_alias="possibleComplication")
    possible_treatment: Rec646fde | list[Rec646fde] | None = Field(default=None, validation_alias="possibleTreatment", serialization_alias="possibleTreatment")
    primary_prevention: MedicalTherapy_Ref | list[MedicalTherapy_Ref] | None = Field(default=None, validation_alias="primaryPrevention", serialization_alias="primaryPrevention")
    risk_factor: MedicalRiskFactor_Ref | list[MedicalRiskFactor_Ref] | None = Field(default=None, validation_alias="riskFactor", serialization_alias="riskFactor")
    secondary_prevention: Rec646fde | list[Rec646fde] | None = Field(default=None, validation_alias="secondaryPrevention", serialization_alias="secondaryPrevention")
    sign_or_symptom: MedicalSignOrSymptom_Ref | list[MedicalSignOrSymptom_Ref] | None = Field(default=None, validation_alias="signOrSymptom", serialization_alias="signOrSymptom")
    stage: MedicalConditionStage_Ref | list[MedicalConditionStage_Ref] | None = Field(default=None)
    status: EventStatusType_MedicalStudyStatus_Text | list[EventStatusType_MedicalStudyStatus_Text] | None = Field(default=None)
    typical_test: MedicalTest_Ref | list[MedicalTest_Ref] | None = Field(default=None, validation_alias="typicalTest", serialization_alias="typicalTest")

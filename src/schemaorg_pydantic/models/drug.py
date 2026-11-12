from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Ref, Text, Url
from .product import Product
from .substance import Substance
from .drug_pregnancy_category import DrugPregnancyCategory
from .drug_prescription_status import DrugPrescriptionStatus

if TYPE_CHECKING:
    from .dose_schedule import DoseSchedule
    from .drug_class import DrugClass
    from .drug_strength import DrugStrength
    from .health_insurance_plan import HealthInsurancePlan

if TYPE_CHECKING:
    DoseSchedule_Ref = Union[DoseSchedule, Ref]
else:
    DoseSchedule_Ref = Union[Is["DoseSchedule"], Ref]

if TYPE_CHECKING:
    Drug_Ref = Union["Drug", Ref]
else:
    Drug_Ref = Union[Is["Drug"], Ref]

if TYPE_CHECKING:
    DrugClass_Ref = Union[DrugClass, Ref]
else:
    DrugClass_Ref = Union[Is["DrugClass"], Ref]

DrugPrescriptionStatus_Text = Union[DrugPrescriptionStatus, Text]
if TYPE_CHECKING:
    DrugStrength_Ref = Union[DrugStrength, Ref]
else:
    DrugStrength_Ref = Union[Is["DrugStrength"], Ref]

if TYPE_CHECKING:
    HealthInsurancePlan_Ref = Union[HealthInsurancePlan, Ref]
else:
    HealthInsurancePlan_Ref = Union[Is["HealthInsurancePlan"], Ref]


class Drug(Product, Substance):
    """A chemical or biologic substance, used as a medical therapy, that has a physiological effect on an organism. Here the term drug is used interchangeably with the term medicine although clinical knowledge makes a clear difference between them."""
    schema_type: ClassVar[str] = "Drug"
    administration_route: Text | list[Text] | None = Field(default=None, validation_alias="administrationRoute", serialization_alias="administrationRoute")
    alcohol_warning: Text | list[Text] | None = Field(default=None, validation_alias="alcoholWarning", serialization_alias="alcoholWarning")
    available_strength: DrugStrength_Ref | list[DrugStrength_Ref] | None = Field(default=None, validation_alias="availableStrength", serialization_alias="availableStrength")
    breastfeeding_warning: Text | list[Text] | None = Field(default=None, validation_alias="breastfeedingWarning", serialization_alias="breastfeedingWarning")
    clinical_pharmacology: Text | list[Text] | None = Field(default=None, validation_alias="clinicalPharmacology", serialization_alias="clinicalPharmacology")
    dosage_form: Text | list[Text] | None = Field(default=None, validation_alias="dosageForm", serialization_alias="dosageForm")
    dose_schedule: DoseSchedule_Ref | list[DoseSchedule_Ref] | None = Field(default=None, validation_alias="doseSchedule", serialization_alias="doseSchedule")
    drug_class: DrugClass_Ref | list[DrugClass_Ref] | None = Field(default=None, validation_alias="drugClass", serialization_alias="drugClass")
    drug_unit: Text | list[Text] | None = Field(default=None, validation_alias="drugUnit", serialization_alias="drugUnit")
    food_warning: Text | list[Text] | None = Field(default=None, validation_alias="foodWarning", serialization_alias="foodWarning")
    included_in_health_insurance_plan: HealthInsurancePlan_Ref | list[HealthInsurancePlan_Ref] | None = Field(default=None, validation_alias="includedInHealthInsurancePlan", serialization_alias="includedInHealthInsurancePlan")
    interacting_drug: Drug_Ref | list[Drug_Ref] | None = Field(default=None, validation_alias="interactingDrug", serialization_alias="interactingDrug")
    is_available_generically: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isAvailableGenerically", serialization_alias="isAvailableGenerically")
    is_proprietary: Boolean | list[Boolean] | None = Field(default=None, validation_alias="isProprietary", serialization_alias="isProprietary")
    label_details: Url | list[Url] | None = Field(default=None, validation_alias="labelDetails", serialization_alias="labelDetails")
    mechanism_of_action: Text | list[Text] | None = Field(default=None, validation_alias="mechanismOfAction", serialization_alias="mechanismOfAction")
    non_proprietary_name: Text | list[Text] | None = Field(default=None, validation_alias="nonProprietaryName", serialization_alias="nonProprietaryName")
    overdosage: Text | list[Text] | None = Field(default=None)
    pregnancy_category: DrugPregnancyCategory | list[DrugPregnancyCategory] | None = Field(default=None, validation_alias="pregnancyCategory", serialization_alias="pregnancyCategory")
    pregnancy_warning: Text | list[Text] | None = Field(default=None, validation_alias="pregnancyWarning", serialization_alias="pregnancyWarning")
    prescribing_info: Url | list[Url] | None = Field(default=None, validation_alias="prescribingInfo", serialization_alias="prescribingInfo")
    prescription_status: DrugPrescriptionStatus_Text | list[DrugPrescriptionStatus_Text] | None = Field(default=None, validation_alias="prescriptionStatus", serialization_alias="prescriptionStatus")
    proprietary_name: Text | list[Text] | None = Field(default=None, validation_alias="proprietaryName", serialization_alias="proprietaryName")
    related_drug: Drug_Ref | list[Drug_Ref] | None = Field(default=None, validation_alias="relatedDrug", serialization_alias="relatedDrug")
    rxcui: Text | list[Text] | None = Field(default=None)
    warning: Text | list[Text] | None = Field(default=None)

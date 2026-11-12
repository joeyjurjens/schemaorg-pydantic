from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .health_plan_cost_sharing_specification import HealthPlanCostSharingSpecification

if TYPE_CHECKING:
    HealthPlanCostSharingSpecification_Boolean_Ref = Union[HealthPlanCostSharingSpecification, Boolean, Ref]
else:
    HealthPlanCostSharingSpecification_Boolean_Ref = Union[Is["HealthPlanCostSharingSpecification"], Boolean, Ref]


class HealthPlanFormulary(Intangible):
    """For a given health insurance plan, the specification for costs and coverage of prescription drugs."""
    schema_type: ClassVar[str] = "HealthPlanFormulary"
    health_plan_cost_sharing: HealthPlanCostSharingSpecification_Boolean_Ref | list[HealthPlanCostSharingSpecification_Boolean_Ref] | None = Field(default=None, validation_alias="healthPlanCostSharing", serialization_alias="healthPlanCostSharing")
    health_plan_drug_tier: Text | list[Text] | None = Field(default=None, validation_alias="healthPlanDrugTier", serialization_alias="healthPlanDrugTier")
    offers_prescription_by_mail: Boolean | list[Boolean] | None = Field(default=None, validation_alias="offersPrescriptionByMail", serialization_alias="offersPrescriptionByMail")

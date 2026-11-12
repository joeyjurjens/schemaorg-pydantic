from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text, Url
from .intangible import Intangible

if TYPE_CHECKING:
    from .contact_point import ContactPoint
    from .health_plan_formulary import HealthPlanFormulary
    from .health_plan_network import HealthPlanNetwork

if TYPE_CHECKING:
    ContactPoint_Ref = Union[ContactPoint, Ref]
else:
    ContactPoint_Ref = Union[Is["ContactPoint"], Ref]

if TYPE_CHECKING:
    HealthPlanFormulary_Ref = Union[HealthPlanFormulary, Ref]
else:
    HealthPlanFormulary_Ref = Union[Is["HealthPlanFormulary"], Ref]

if TYPE_CHECKING:
    HealthPlanNetwork_Ref = Union[HealthPlanNetwork, Ref]
else:
    HealthPlanNetwork_Ref = Union[Is["HealthPlanNetwork"], Ref]


class HealthInsurancePlan(Intangible):
    """A US-style health insurance plan, including PPOs, EPOs, and HMOs."""
    schema_type: ClassVar[str] = "HealthInsurancePlan"
    benefits_summary_url: Url | list[Url] | None = Field(default=None, validation_alias="benefitsSummaryUrl", serialization_alias="benefitsSummaryUrl")
    contact_point: ContactPoint_Ref | list[ContactPoint_Ref] | None = Field(default=None, validation_alias="contactPoint", serialization_alias="contactPoint")
    health_plan_drug_option: Text | list[Text] | None = Field(default=None, validation_alias="healthPlanDrugOption", serialization_alias="healthPlanDrugOption")
    health_plan_drug_tier: Text | list[Text] | None = Field(default=None, validation_alias="healthPlanDrugTier", serialization_alias="healthPlanDrugTier")
    health_plan_id: Text | list[Text] | None = Field(default=None, validation_alias="healthPlanId", serialization_alias="healthPlanId")
    health_plan_marketing_url: Url | list[Url] | None = Field(default=None, validation_alias="healthPlanMarketingUrl", serialization_alias="healthPlanMarketingUrl")
    includes_health_plan_formulary: HealthPlanFormulary_Ref | list[HealthPlanFormulary_Ref] | None = Field(default=None, validation_alias="includesHealthPlanFormulary", serialization_alias="includesHealthPlanFormulary")
    includes_health_plan_network: HealthPlanNetwork_Ref | list[HealthPlanNetwork_Ref] | None = Field(default=None, validation_alias="includesHealthPlanNetwork", serialization_alias="includesHealthPlanNetwork")
    uses_health_plan_id_standard: Text | list[Text] | None = Field(default=None, validation_alias="usesHealthPlanIdStandard", serialization_alias="usesHealthPlanIdStandard")

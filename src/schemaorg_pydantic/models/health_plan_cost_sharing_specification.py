from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .price_specification import PriceSpecification

if TYPE_CHECKING:
    PriceSpecification_Ref = Union[PriceSpecification, Ref]
else:
    PriceSpecification_Ref = Union[Is["PriceSpecification"], Ref]


class HealthPlanCostSharingSpecification(Intangible):
    """A description of costs to the patient under a given network or formulary."""
    schema_type: ClassVar[str] = "HealthPlanCostSharingSpecification"
    health_plan_coinsurance_option: Text | list[Text] | None = Field(default=None, validation_alias="healthPlanCoinsuranceOption", serialization_alias="healthPlanCoinsuranceOption")
    health_plan_coinsurance_rate: Number | list[Number] | None = Field(default=None, validation_alias="healthPlanCoinsuranceRate", serialization_alias="healthPlanCoinsuranceRate")
    health_plan_copay: PriceSpecification_Ref | list[PriceSpecification_Ref] | None = Field(default=None, validation_alias="healthPlanCopay", serialization_alias="healthPlanCopay")
    health_plan_copay_option: Text | list[Text] | None = Field(default=None, validation_alias="healthPlanCopayOption", serialization_alias="healthPlanCopayOption")
    health_plan_pharmacy_category: Text | list[Text] | None = Field(default=None, validation_alias="healthPlanPharmacyCategory", serialization_alias="healthPlanPharmacyCategory")

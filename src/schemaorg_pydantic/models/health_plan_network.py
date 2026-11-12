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


class HealthPlanNetwork(Intangible):
    """A US-style health insurance plan network."""
    schema_type: ClassVar[str] = "HealthPlanNetwork"
    health_plan_cost_sharing: HealthPlanCostSharingSpecification_Boolean_Ref | list[HealthPlanCostSharingSpecification_Boolean_Ref] | None = Field(default=None, validation_alias="healthPlanCostSharing", serialization_alias="healthPlanCostSharing")
    health_plan_network_id: Text | list[Text] | None = Field(default=None, validation_alias="healthPlanNetworkId", serialization_alias="healthPlanNetworkId")
    health_plan_network_tier: Text | list[Text] | None = Field(default=None, validation_alias="healthPlanNetworkTier", serialization_alias="healthPlanNetworkTier")

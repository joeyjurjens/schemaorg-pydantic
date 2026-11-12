from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .intangible import Intangible
from .tier_benefit_enumeration import TierBenefitEnumeration

if TYPE_CHECKING:
    from .credit_card import CreditCard
    from .member_program import MemberProgram
    from .monetary_amount import MonetaryAmount
    from .quantitative_value import QuantitativeValue
    from .unit_price_specification import UnitPriceSpecification

if TYPE_CHECKING:
    R30df5581 = Union[CreditCard, MonetaryAmount, UnitPriceSpecification, Text, Ref]
else:
    R30df5581 = Union[Is["CreditCard"], Is["MonetaryAmount"], Is["UnitPriceSpecification"], Text, Ref]

if TYPE_CHECKING:
    MemberProgram_Ref = Union[MemberProgram, Ref]
else:
    MemberProgram_Ref = Union[Is["MemberProgram"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]


class MemberProgramTier(Intangible):
    """A MemberProgramTier specifies a tier under a loyalty (member) program, for example \"gold\"."""
    schema_type: ClassVar[str] = "MemberProgramTier"
    has_tier_benefit: TierBenefitEnumeration | list[TierBenefitEnumeration] | None = Field(default=None, validation_alias="hasTierBenefit", serialization_alias="hasTierBenefit")
    has_tier_requirement: R30df5581 | list[R30df5581] | None = Field(default=None, validation_alias="hasTierRequirement", serialization_alias="hasTierRequirement")
    is_tier_of: MemberProgram_Ref | list[MemberProgram_Ref] | None = Field(default=None, validation_alias="isTierOf", serialization_alias="isTierOf")
    membership_points_earned: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="membershipPointsEarned", serialization_alias="membershipPointsEarned")

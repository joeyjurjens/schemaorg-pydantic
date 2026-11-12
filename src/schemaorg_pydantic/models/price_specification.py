from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, DateTime, Is, Number, Ref, Text
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .member_program_tier import MemberProgramTier
    from .quantitative_value import QuantitativeValue

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    MemberProgramTier_Ref = Union[MemberProgramTier, Ref]
else:
    MemberProgramTier_Ref = Union[Is["MemberProgramTier"], Ref]

Number_Text = Union[Number, Text]
if TYPE_CHECKING:
    PriceSpecification_Ref = Union["PriceSpecification", Ref]
else:
    PriceSpecification_Ref = Union[Is["PriceSpecification"], Ref]

if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]


class PriceSpecification(StructuredValue):
    """A structured value representing a price or price range. Typically, only the subclasses of this type are used for markup. It is recommended to use [[MonetaryAmount]] to describe independent amounts of money such as a salary, credit card limits, etc."""
    schema_type: ClassVar[str] = "PriceSpecification"
    eligible_quantity: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="eligibleQuantity", serialization_alias="eligibleQuantity")
    eligible_transaction_volume: PriceSpecification_Ref | list[PriceSpecification_Ref] | None = Field(default=None, validation_alias="eligibleTransactionVolume", serialization_alias="eligibleTransactionVolume")
    max_price: Number | list[Number] | None = Field(default=None, validation_alias="maxPrice", serialization_alias="maxPrice")
    membership_points_earned: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="membershipPointsEarned", serialization_alias="membershipPointsEarned")
    min_price: Number | list[Number] | None = Field(default=None, validation_alias="minPrice", serialization_alias="minPrice")
    price: Number_Text | list[Number_Text] | None = Field(default=None)
    price_currency: Text | list[Text] | None = Field(default=None, validation_alias="priceCurrency", serialization_alias="priceCurrency")
    valid_for_member_tier: MemberProgramTier_Ref | list[MemberProgramTier_Ref] | None = Field(default=None, validation_alias="validForMemberTier", serialization_alias="validForMemberTier")
    valid_from: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validFrom", serialization_alias="validFrom")
    valid_through: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validThrough", serialization_alias="validThrough")
    value_added_tax_included: Boolean | list[Boolean] | None = Field(default=None, validation_alias="valueAddedTaxIncluded", serialization_alias="valueAddedTaxIncluded")

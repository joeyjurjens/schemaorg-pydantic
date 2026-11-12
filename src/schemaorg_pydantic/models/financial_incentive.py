from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref, Text
from .intangible import Intangible
from .incentive_qualified_expense_type import IncentiveQualifiedExpenseType
from .incentive_status import IncentiveStatus
from .incentive_type import IncentiveType
from .purchase_type import PurchaseType

if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .defined_term import DefinedTerm
    from .geo_shape import GeoShape
    from .loan_or_credit import LoanOrCredit
    from .monetary_amount import MonetaryAmount
    from .organization import Organization
    from .person import Person
    from .place import Place
    from .product import Product
    from .quantitative_value import QuantitativeValue
    from .unit_price_specification import UnitPriceSpecification

if TYPE_CHECKING:
    R3fcc4ec8 = Union[AdministrativeArea, GeoShape, Place, Text, Ref]
else:
    R3fcc4ec8 = Union[Is["AdministrativeArea"], Is["GeoShape"], Is["Place"], Text, Ref]

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    DefinedTerm_Product_Ref = Union[DefinedTerm, Product, Ref]
else:
    DefinedTerm_Product_Ref = Union[Is["DefinedTerm"], Is["Product"], Ref]

if TYPE_CHECKING:
    LoanOrCredit_QuantitativeValue_UnitPriceSpecification_Ref = Union[LoanOrCredit, QuantitativeValue, UnitPriceSpecification, Ref]
else:
    LoanOrCredit_QuantitativeValue_UnitPriceSpecification_Ref = Union[Is["LoanOrCredit"], Is["QuantitativeValue"], Is["UnitPriceSpecification"], Ref]

if TYPE_CHECKING:
    MonetaryAmount_Ref = Union[MonetaryAmount, Ref]
else:
    MonetaryAmount_Ref = Union[Is["MonetaryAmount"], Ref]

if TYPE_CHECKING:
    MonetaryAmount_Text_Ref = Union[MonetaryAmount, Text, Ref]
else:
    MonetaryAmount_Text_Ref = Union[Is["MonetaryAmount"], Text, Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    Organization_Ref = Union[Organization, Ref]
else:
    Organization_Ref = Union[Is["Organization"], Ref]


class FinancialIncentive(Intangible):
    """<p>Represents financial incentives for goods/services offered by an organization (or individual).</p>"""
    schema_type: ClassVar[str] = "FinancialIncentive"
    area_served: R3fcc4ec8 | list[R3fcc4ec8] | None = Field(default=None, validation_alias="areaServed", serialization_alias="areaServed")
    eligible_with_supplier: Organization_Ref | list[Organization_Ref] | None = Field(default=None, validation_alias="eligibleWithSupplier", serialization_alias="eligibleWithSupplier")
    incentive_amount: LoanOrCredit_QuantitativeValue_UnitPriceSpecification_Ref | list[LoanOrCredit_QuantitativeValue_UnitPriceSpecification_Ref] | None = Field(default=None, validation_alias="incentiveAmount", serialization_alias="incentiveAmount")
    incentive_status: IncentiveStatus | list[IncentiveStatus] | None = Field(default=None, validation_alias="incentiveStatus", serialization_alias="incentiveStatus")
    incentive_type: IncentiveType | list[IncentiveType] | None = Field(default=None, validation_alias="incentiveType", serialization_alias="incentiveType")
    incentivized_item: DefinedTerm_Product_Ref | list[DefinedTerm_Product_Ref] | None = Field(default=None, validation_alias="incentivizedItem", serialization_alias="incentivizedItem")
    income_limit: MonetaryAmount_Text_Ref | list[MonetaryAmount_Text_Ref] | None = Field(default=None, validation_alias="incomeLimit", serialization_alias="incomeLimit")
    provider: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    publisher: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    purchase_price_limit: MonetaryAmount_Ref | list[MonetaryAmount_Ref] | None = Field(default=None, validation_alias="purchasePriceLimit", serialization_alias="purchasePriceLimit")
    purchase_type: PurchaseType | list[PurchaseType] | None = Field(default=None, validation_alias="purchaseType", serialization_alias="purchaseType")
    qualified_expense: IncentiveQualifiedExpenseType | list[IncentiveQualifiedExpenseType] | None = Field(default=None, validation_alias="qualifiedExpense", serialization_alias="qualifiedExpense")
    valid_from: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validFrom", serialization_alias="validFrom")
    valid_through: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validThrough", serialization_alias="validThrough")

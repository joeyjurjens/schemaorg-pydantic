from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .service import Service

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]


class FinancialProduct(Service):
    """A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry."""
    schema_type: ClassVar[str] = "FinancialProduct"
    annual_percentage_rate: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="annualPercentageRate", serialization_alias="annualPercentageRate")
    fees_and_commissions_specification: Text | list[Text] | None = Field(default=None, validation_alias="feesAndCommissionsSpecification", serialization_alias="feesAndCommissionsSpecification")
    interest_rate: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="interestRate", serialization_alias="interestRate")

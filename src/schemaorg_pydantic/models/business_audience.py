from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .audience import Audience

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]


class BusinessAudience(Audience):
    """A set of characteristics belonging to businesses, e.g. who compose an item's target audience."""
    schema_type: ClassVar[str] = "BusinessAudience"
    number_of_employees: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="numberOfEmployees", serialization_alias="numberOfEmployees")
    yearly_revenue: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="yearlyRevenue", serialization_alias="yearlyRevenue")
    years_in_operation: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="yearsInOperation", serialization_alias="yearsInOperation")

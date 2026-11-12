from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .organization_role import OrganizationRole

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount
    from .price_specification import PriceSpecification

if TYPE_CHECKING:
    MonetaryAmount_PriceSpecification_Number_Ref = Union[MonetaryAmount, PriceSpecification, Number, Ref]
else:
    MonetaryAmount_PriceSpecification_Number_Ref = Union[Is["MonetaryAmount"], Is["PriceSpecification"], Number, Ref]


class EmployeeRole(OrganizationRole):
    """A subclass of OrganizationRole used to describe employee relationships."""
    schema_type: ClassVar[str] = "EmployeeRole"
    base_salary: MonetaryAmount_PriceSpecification_Number_Ref | list[MonetaryAmount_PriceSpecification_Number_Ref] | None = Field(default=None, validation_alias="baseSalary", serialization_alias="baseSalary")
    salary_currency: Text | list[Text] | None = Field(default=None, validation_alias="salaryCurrency", serialization_alias="salaryCurrency")

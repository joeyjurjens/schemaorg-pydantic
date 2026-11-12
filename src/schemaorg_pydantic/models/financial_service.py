from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .local_business import LocalBusiness


class FinancialService(LocalBusiness):
    """Financial services business."""
    schema_type: ClassVar[str] = "FinancialService"
    fees_and_commissions_specification: Text | list[Text] | None = Field(default=None, validation_alias="feesAndCommissionsSpecification", serialization_alias="feesAndCommissionsSpecification")

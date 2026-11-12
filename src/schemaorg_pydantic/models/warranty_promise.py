from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .warranty_scope import WarrantyScope

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]

if TYPE_CHECKING:
    WarrantyScope_Ref = Union[WarrantyScope, Ref]
else:
    WarrantyScope_Ref = Union[Is["WarrantyScope"], Ref]


class WarrantyPromise(StructuredValue):
    """A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product."""
    schema_type: ClassVar[str] = "WarrantyPromise"
    duration_of_warranty: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="durationOfWarranty", serialization_alias="durationOfWarranty")
    warranty_scope: WarrantyScope_Ref | list[WarrantyScope_Ref] | None = Field(default=None, validation_alias="warrantyScope", serialization_alias="warrantyScope")

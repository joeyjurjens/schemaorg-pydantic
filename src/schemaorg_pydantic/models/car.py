from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .vehicle import Vehicle

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    QuantitativeValue_Ref = Union[QuantitativeValue, Ref]
else:
    QuantitativeValue_Ref = Union[Is["QuantitativeValue"], Ref]


class Car(Vehicle):
    """A car is a wheeled, self-powered motor vehicle used for transportation."""
    schema_type: ClassVar[str] = "Car"
    acriss_code: Text | list[Text] | None = Field(default=None, validation_alias="acrissCode", serialization_alias="acrissCode")
    roof_load: QuantitativeValue_Ref | list[QuantitativeValue_Ref] | None = Field(default=None, validation_alias="roofLoad", serialization_alias="roofLoad")

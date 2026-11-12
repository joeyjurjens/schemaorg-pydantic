from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class QuantitativeValueDistribution(StructuredValue):
    """A statistical distribution of values."""
    schema_type: ClassVar[str] = "QuantitativeValueDistribution"
    duration: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None)
    median: Number | list[Number] | None = Field(default=None)
    percentile_10: Number | list[Number] | None = Field(default=None, validation_alias="percentile10", serialization_alias="percentile10")
    percentile_25: Number | list[Number] | None = Field(default=None, validation_alias="percentile25", serialization_alias="percentile25")
    percentile_75: Number | list[Number] | None = Field(default=None, validation_alias="percentile75", serialization_alias="percentile75")
    percentile_90: Number | list[Number] | None = Field(default=None, validation_alias="percentile90", serialization_alias="percentile90")

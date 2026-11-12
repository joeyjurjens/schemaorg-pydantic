from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref, Text
from .web_page import WebPage

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class RealEstateListing(WebPage):
    """A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s (whose [[businessFunction]] is typically to lease out, or to sell).\n  The [[RealEstateListing]] type itself represents the overall listing, as manifested in some [[WebPage]]."""
    schema_type: ClassVar[str] = "RealEstateListing"
    date_posted: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="datePosted", serialization_alias="datePosted")
    lease_length: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="leaseLength", serialization_alias="leaseLength")

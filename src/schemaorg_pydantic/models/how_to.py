from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .how_to_section import HowToSection
    from .how_to_step import HowToStep
    from .how_to_supply import HowToSupply
    from .how_to_tool import HowToTool
    from .monetary_amount import MonetaryAmount
    from .quantitative_value import QuantitativeValue

if TYPE_CHECKING:
    R62f9cd91 = Union[CreativeWork, HowToSection, HowToStep, Text, Ref]
else:
    R62f9cd91 = Union[Is["CreativeWork"], Is["HowToSection"], Is["HowToStep"], Text, Ref]

if TYPE_CHECKING:
    HowToSupply_Text_Ref = Union[HowToSupply, Text, Ref]
else:
    HowToSupply_Text_Ref = Union[Is["HowToSupply"], Text, Ref]

if TYPE_CHECKING:
    HowToTool_Text_Ref = Union[HowToTool, Text, Ref]
else:
    HowToTool_Text_Ref = Union[Is["HowToTool"], Text, Ref]

if TYPE_CHECKING:
    MonetaryAmount_Text_Ref = Union[MonetaryAmount, Text, Ref]
else:
    MonetaryAmount_Text_Ref = Union[Is["MonetaryAmount"], Text, Ref]

if TYPE_CHECKING:
    QuantitativeValue_Text_Ref = Union[QuantitativeValue, Text, Ref]
else:
    QuantitativeValue_Text_Ref = Union[Is["QuantitativeValue"], Text, Ref]


class HowTo(CreativeWork):
    """Instructions that explain how to achieve a result by performing a sequence of steps."""
    schema_type: ClassVar[str] = "HowTo"
    estimated_cost: MonetaryAmount_Text_Ref | list[MonetaryAmount_Text_Ref] | None = Field(default=None, validation_alias="estimatedCost", serialization_alias="estimatedCost")
    perform_time: Text | list[Text] | None = Field(default=None, validation_alias="performTime", serialization_alias="performTime")
    prep_time: Text | list[Text] | None = Field(default=None, validation_alias="prepTime", serialization_alias="prepTime")
    step: R62f9cd91 | list[R62f9cd91] | None = Field(default=None)
    supply: HowToSupply_Text_Ref | list[HowToSupply_Text_Ref] | None = Field(default=None)
    tool: HowToTool_Text_Ref | list[HowToTool_Text_Ref] | None = Field(default=None)
    total_time: Text | list[Text] | None = Field(default=None, validation_alias="totalTime", serialization_alias="totalTime")
    yield_: QuantitativeValue_Text_Ref | list[QuantitativeValue_Text_Ref] | None = Field(default=None, validation_alias="yield", serialization_alias="yield")

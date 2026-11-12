from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .review import Review
from .physical_activity_category import PhysicalActivityCategory

if TYPE_CHECKING:
    from .category_code import CategoryCode
    from .thing import Thing

if TYPE_CHECKING:
    R88d1e012 = Union[CategoryCode, PhysicalActivityCategory, Thing, Text, Ref]
else:
    R88d1e012 = Union[Is["CategoryCode"], PhysicalActivityCategory, Is["Thing"], Text, Ref]


class Recommendation(Review):
    """[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the best option or best course of action. Recommendations may be for products or services, or other concrete things, as in the case of a ranked list or product guide. A [[Guide]] may list multiple recommendations for different categories. For example, in a [[Guide]] about which TVs to buy, the author may have several [[Recommendation]]s."""
    schema_type: ClassVar[str] = "Recommendation"
    category: R88d1e012 | list[R88d1e012] | None = Field(default=None)

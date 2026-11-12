from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .creative_work import CreativeWork
from .physical_activity_category import PhysicalActivityCategory

if TYPE_CHECKING:
    from .category_code import CategoryCode
    from .structured_value import StructuredValue
    from .thing import Thing

if TYPE_CHECKING:
    R88d1e012 = Union[CategoryCode, PhysicalActivityCategory, Thing, Text, Ref]
else:
    R88d1e012 = Union[Is["CategoryCode"], PhysicalActivityCategory, Is["Thing"], Text, Ref]

if TYPE_CHECKING:
    StructuredValue_Text_Ref = Union[StructuredValue, Text, Ref]
else:
    StructuredValue_Text_Ref = Union[Is["StructuredValue"], Text, Ref]


class Guide(CreativeWork):
    """[[Guide]] is a page or article that recommends specific products or services, or aspects of a thing for a user to consider. A [[Guide]] may represent a Buying Guide and detail aspects of products or services for a user to consider. A [[Guide]] may represent a Product Guide and recommend specific products or services. A [[Guide]] may represent a Ranked List and recommend specific products or services with ranking."""
    schema_type: ClassVar[str] = "Guide"
    category: R88d1e012 | list[R88d1e012] | None = Field(default=None)
    review_aspect: StructuredValue_Text_Ref | list[StructuredValue_Text_Ref] | None = Field(default=None, validation_alias="reviewAspect", serialization_alias="reviewAspect")

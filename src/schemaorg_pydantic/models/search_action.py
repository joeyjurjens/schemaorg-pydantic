from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .action import Action

if TYPE_CHECKING:
    from .property_value_specification import PropertyValueSpecification

if TYPE_CHECKING:
    PropertyValueSpecification_Text_Ref = Union[PropertyValueSpecification, Text, Ref]
else:
    PropertyValueSpecification_Text_Ref = Union[Is["PropertyValueSpecification"], Text, Ref]


class SearchAction(Action):
    """The act of searching for an object."""
    schema_type: ClassVar[str] = "SearchAction"
    query: Text | list[Text] | None = Field(default=None)
    query_input: PropertyValueSpecification_Text_Ref | list[PropertyValueSpecification_Text_Ref] | None = Field(default=None, validation_alias="query-input", serialization_alias="query-input")

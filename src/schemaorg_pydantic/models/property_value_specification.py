from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Is, Number, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .thing import Thing

if TYPE_CHECKING:
    Thing_Text_Ref = Union[Thing, Text, Ref]
else:
    Thing_Text_Ref = Union[Is["Thing"], Text, Ref]


class PropertyValueSpecification(Intangible):
    """A Property value specification."""
    schema_type: ClassVar[str] = "PropertyValueSpecification"
    default_value: Thing_Text_Ref | list[Thing_Text_Ref] | None = Field(default=None, validation_alias="defaultValue", serialization_alias="defaultValue")
    max_value: Number | list[Number] | None = Field(default=None, validation_alias="maxValue", serialization_alias="maxValue")
    min_value: Number | list[Number] | None = Field(default=None, validation_alias="minValue", serialization_alias="minValue")
    multiple_values: Boolean | list[Boolean] | None = Field(default=None, validation_alias="multipleValues", serialization_alias="multipleValues")
    readonly_value: Boolean | list[Boolean] | None = Field(default=None, validation_alias="readonlyValue", serialization_alias="readonlyValue")
    step_value: Number | list[Number] | None = Field(default=None, validation_alias="stepValue", serialization_alias="stepValue")
    value_max_length: Number | list[Number] | None = Field(default=None, validation_alias="valueMaxLength", serialization_alias="valueMaxLength")
    value_min_length: Number | list[Number] | None = Field(default=None, validation_alias="valueMinLength", serialization_alias="valueMinLength")
    value_name: Text | list[Text] | None = Field(default=None, validation_alias="valueName", serialization_alias="valueName")
    value_pattern: Text | list[Text] | None = Field(default=None, validation_alias="valuePattern", serialization_alias="valuePattern")
    value_required: Boolean | list[Boolean] | None = Field(default=None, validation_alias="valueRequired", serialization_alias="valueRequired")

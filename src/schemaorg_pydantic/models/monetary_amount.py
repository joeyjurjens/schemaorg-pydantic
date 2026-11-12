from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Boolean, Date, DateTime, Is, Number, Ref, Text
from .structured_value import StructuredValue
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .steering_position_value import SteeringPositionValue

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    R3f96830d = Union[DriveWheelConfigurationValue, SteeringPositionValue, StructuredValue, Boolean, Number, Text, Ref]
else:
    R3f96830d = Union[DriveWheelConfigurationValue, SteeringPositionValue, Is["StructuredValue"], Boolean, Number, Text, Ref]


class MonetaryAmount(StructuredValue):
    """A monetary value or range. This type can be used to describe an amount of money such as $50 USD, or a range as in describing a bank account being suitable for a balance between \u00a31,000 and \u00a31,000,000 GBP, or the value of a salary, etc. It is recommended to use [[PriceSpecification]] Types to describe the price of an Offer, Invoice, etc."""
    schema_type: ClassVar[str] = "MonetaryAmount"
    currency: Text | list[Text] | None = Field(default=None)
    max_value: Number | list[Number] | None = Field(default=None, validation_alias="maxValue", serialization_alias="maxValue")
    min_value: Number | list[Number] | None = Field(default=None, validation_alias="minValue", serialization_alias="minValue")
    valid_from: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validFrom", serialization_alias="validFrom")
    valid_through: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="validThrough", serialization_alias="validThrough")
    value: R3f96830d | list[R3f96830d] | None = Field(default=None)

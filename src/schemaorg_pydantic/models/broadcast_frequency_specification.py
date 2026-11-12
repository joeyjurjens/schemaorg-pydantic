from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .intangible import Intangible
from .drive_wheel_configuration_value import DriveWheelConfigurationValue
from .steering_position_value import SteeringPositionValue

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

DriveWheelConfigurationValue_SteeringPositionValue_Text = Union[DriveWheelConfigurationValue, SteeringPositionValue, Text]
if TYPE_CHECKING:
    QuantitativeValue_Number_Ref = Union[QuantitativeValue, Number, Ref]
else:
    QuantitativeValue_Number_Ref = Union[Is["QuantitativeValue"], Number, Ref]


class BroadcastFrequencySpecification(Intangible):
    """The frequency in MHz and the modulation used for a particular BroadcastService."""
    schema_type: ClassVar[str] = "BroadcastFrequencySpecification"
    broadcast_frequency_value: QuantitativeValue_Number_Ref | list[QuantitativeValue_Number_Ref] | None = Field(default=None, validation_alias="broadcastFrequencyValue", serialization_alias="broadcastFrequencyValue")
    broadcast_signal_modulation: DriveWheelConfigurationValue_SteeringPositionValue_Text | list[DriveWheelConfigurationValue_SteeringPositionValue_Text] | None = Field(default=None, validation_alias="broadcastSignalModulation", serialization_alias="broadcastSignalModulation")
    broadcast_sub_channel: Text | list[Text] | None = Field(default=None, validation_alias="broadcastSubChannel", serialization_alias="broadcastSubChannel")

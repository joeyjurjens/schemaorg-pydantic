from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Ref, Text
from .intangible import Intangible

if TYPE_CHECKING:
    from .broadcast_frequency_specification import BroadcastFrequencySpecification
    from .broadcast_service import BroadcastService
    from .cable_or_satellite_service import CableOrSatelliteService
    from .defined_term import DefinedTerm

if TYPE_CHECKING:
    BroadcastFrequencySpecification_Text_Ref = Union[BroadcastFrequencySpecification, Text, Ref]
else:
    BroadcastFrequencySpecification_Text_Ref = Union[Is["BroadcastFrequencySpecification"], Text, Ref]

if TYPE_CHECKING:
    BroadcastService_Ref = Union[BroadcastService, Ref]
else:
    BroadcastService_Ref = Union[Is["BroadcastService"], Ref]

if TYPE_CHECKING:
    CableOrSatelliteService_Ref = Union[CableOrSatelliteService, Ref]
else:
    CableOrSatelliteService_Ref = Union[Is["CableOrSatelliteService"], Ref]

if TYPE_CHECKING:
    DefinedTerm_Text_Ref = Union[DefinedTerm, Text, Ref]
else:
    DefinedTerm_Text_Ref = Union[Is["DefinedTerm"], Text, Ref]


class BroadcastChannel(Intangible):
    """A unique instance of a BroadcastService on a CableOrSatelliteService lineup."""
    schema_type: ClassVar[str] = "BroadcastChannel"
    broadcast_channel_id: Text | list[Text] | None = Field(default=None, validation_alias="broadcastChannelId", serialization_alias="broadcastChannelId")
    broadcast_frequency: BroadcastFrequencySpecification_Text_Ref | list[BroadcastFrequencySpecification_Text_Ref] | None = Field(default=None, validation_alias="broadcastFrequency", serialization_alias="broadcastFrequency")
    broadcast_service_tier: Text | list[Text] | None = Field(default=None, validation_alias="broadcastServiceTier", serialization_alias="broadcastServiceTier")
    genre: DefinedTerm_Text_Ref | list[DefinedTerm_Text_Ref] | None = Field(default=None)
    in_broadcast_lineup: CableOrSatelliteService_Ref | list[CableOrSatelliteService_Ref] | None = Field(default=None, validation_alias="inBroadcastLineup", serialization_alias="inBroadcastLineup")
    provides_broadcast_service: BroadcastService_Ref | list[BroadcastService_Ref] | None = Field(default=None, validation_alias="providesBroadcastService", serialization_alias="providesBroadcastService")

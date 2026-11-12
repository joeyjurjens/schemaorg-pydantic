from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .broadcast_channel import BroadcastChannel


class RadioChannel(BroadcastChannel):
    """A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup."""
    schema_type: ClassVar[str] = "RadioChannel"

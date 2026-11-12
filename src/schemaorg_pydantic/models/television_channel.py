from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .broadcast_channel import BroadcastChannel


class TelevisionChannel(BroadcastChannel):
    """A unique instance of a television BroadcastService on a CableOrSatelliteService lineup."""
    schema_type: ClassVar[str] = "TelevisionChannel"

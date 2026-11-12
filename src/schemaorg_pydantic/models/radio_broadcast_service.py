from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .broadcast_service import BroadcastService


class RadioBroadcastService(BroadcastService):
    """A delivery service through which radio content is provided via broadcast over the air or online."""
    schema_type: ClassVar[str] = "RadioBroadcastService"

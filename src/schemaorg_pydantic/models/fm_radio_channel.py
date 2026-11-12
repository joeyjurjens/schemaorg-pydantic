from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .radio_channel import RadioChannel


class FMRadioChannel(RadioChannel):
    """A radio channel that uses FM."""
    schema_type: ClassVar[str] = "FMRadioChannel"

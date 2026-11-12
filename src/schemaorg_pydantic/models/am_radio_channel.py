from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .radio_channel import RadioChannel


class AMRadioChannel(RadioChannel):
    """A radio channel that uses AM."""
    schema_type: ClassVar[str] = "AMRadioChannel"

from __future__ import annotations

from typing import ClassVar, Union

from pydantic import Field

from ..base import Text
from .consume_action import ConsumeAction
from .game_availability_enumeration import GameAvailabilityEnumeration

GameAvailabilityEnumeration_Text = Union[GameAvailabilityEnumeration, Text]

class PlayGameAction(ConsumeAction):
    """The act of playing a video game."""
    schema_type: ClassVar[str] = "PlayGameAction"
    game_availability_type: GameAvailabilityEnumeration_Text | list[GameAvailabilityEnumeration_Text] | None = Field(default=None, validation_alias="gameAvailabilityType", serialization_alias="gameAvailabilityType")

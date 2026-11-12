from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork


class Conversation(CreativeWork):
    """One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart properties."""
    schema_type: ClassVar[str] = "Conversation"

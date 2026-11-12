from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .event import Event


class Hackathon(Event):
    """A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event."""
    schema_type: ClassVar[str] = "Hackathon"

from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork


class Poster(CreativeWork):
    """A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise or publicize something."""
    schema_type: ClassVar[str] = "Poster"

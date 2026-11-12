from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .create_action import CreateAction


class FilmAction(CreateAction):
    """The act of capturing sound and moving images on film, video, or digitally."""
    schema_type: ClassVar[str] = "FilmAction"

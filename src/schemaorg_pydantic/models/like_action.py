from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .react_action import ReactAction


class LikeAction(ReactAction):
    """The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants."""
    schema_type: ClassVar[str] = "LikeAction"

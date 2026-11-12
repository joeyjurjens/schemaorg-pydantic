from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .react_action import ReactAction


class DislikeAction(ReactAction):
    """The act of expressing a negative sentiment about the object. An agent dislikes an object (a proposition, topic or theme) with participants."""
    schema_type: ClassVar[str] = "DislikeAction"

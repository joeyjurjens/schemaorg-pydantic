from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .react_action import ReactAction


class AgreeAction(ReactAction):
    """The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants."""
    schema_type: ClassVar[str] = "AgreeAction"

from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .react_action import ReactAction


class DisagreeAction(ReactAction):
    """The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition, topic or theme) with participants."""
    schema_type: ClassVar[str] = "DisagreeAction"

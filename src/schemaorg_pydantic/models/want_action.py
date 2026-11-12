from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .react_action import ReactAction


class WantAction(ReactAction):
    """The act of expressing a desire about the object. An agent wants an object."""
    schema_type: ClassVar[str] = "WantAction"

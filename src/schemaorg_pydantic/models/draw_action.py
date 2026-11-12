from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .create_action import CreateAction


class DrawAction(CreateAction):
    """The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments."""
    schema_type: ClassVar[str] = "DrawAction"

from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .create_action import CreateAction


class PhotographAction(CreateAction):
    """The act of capturing still images of objects using a camera."""
    schema_type: ClassVar[str] = "PhotographAction"

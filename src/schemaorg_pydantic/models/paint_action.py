from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .create_action import CreateAction


class PaintAction(CreateAction):
    """The act of producing a painting, typically with paint and canvas as instruments."""
    schema_type: ClassVar[str] = "PaintAction"

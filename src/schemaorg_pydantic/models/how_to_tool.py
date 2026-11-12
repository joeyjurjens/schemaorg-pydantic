from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .how_to_item import HowToItem


class HowToTool(HowToItem):
    """A tool used (but not consumed) when performing instructions for how to achieve a result."""
    schema_type: ClassVar[str] = "HowToTool"

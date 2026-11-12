from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .find_action import FindAction


class DiscoverAction(FindAction):
    """The act of discovering/finding an object."""
    schema_type: ClassVar[str] = "DiscoverAction"

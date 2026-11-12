from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .action import Action


class FindAction(Action):
    """The act of finding an object."""
    schema_type: ClassVar[str] = "FindAction"

from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from ..base import Text
from .action import Action


class SearchAction(Action):
    """The act of searching for an object."""
    schema_type: ClassVar[str] = "SearchAction"
    query: Text | list[Text] | None = Field(default=None)

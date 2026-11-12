from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .creative_work import CreativeWork
from .list_item import ListItem


class HowToTip(CreativeWork, ListItem):
    """An explanation in the instructions for how to achieve a result. It provides supplementary information about a technique, supply, author's preference, etc. It can explain what could be done, or what should not be done, but doesn't specify what should be done (see HowToDirection)."""
    schema_type: ClassVar[str] = "HowToTip"

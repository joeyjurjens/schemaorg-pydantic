from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .organize_action import OrganizeAction


class BookmarkAction(OrganizeAction):
    """An agent bookmarks/flags/labels/tags/marks an object."""
    schema_type: ClassVar[str] = "BookmarkAction"

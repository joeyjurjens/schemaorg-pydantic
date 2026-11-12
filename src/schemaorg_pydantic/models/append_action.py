from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .insert_action import InsertAction


class AppendAction(InsertAction):
    """The act of inserting at the end if an ordered collection."""
    schema_type: ClassVar[str] = "AppendAction"

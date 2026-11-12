from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .action import Action


class CreateAction(Action):
    """The act of deliberately creating/producing/generating/building a result out of the agent."""
    schema_type: ClassVar[str] = "CreateAction"

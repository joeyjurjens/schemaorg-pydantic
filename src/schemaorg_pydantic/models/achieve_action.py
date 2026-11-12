from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .action import Action


class AchieveAction(Action):
    """The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process."""
    schema_type: ClassVar[str] = "AchieveAction"

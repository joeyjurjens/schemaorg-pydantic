from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .enumeration import Enumeration


class Specialty(Enumeration):
    """Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort."""
    schema_type: ClassVar[str] = "Specialty"

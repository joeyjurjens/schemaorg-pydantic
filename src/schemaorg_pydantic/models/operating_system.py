from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .software_application import SoftwareApplication


class OperatingSystem(SoftwareApplication):
    """System software that manages computer hardware and software resources, and provides common services for computer programs."""
    schema_type: ClassVar[str] = "OperatingSystem"
